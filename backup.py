import os
import subprocess
from datetime import datetime
import shutil
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('backup.log'),
        logging.StreamHandler()
    ]
)

# Configuration
BACKUP_DIR = Path('/path/to/backups')
DB_NAME = 'db.sqlite3'
MEDIA_DIR = Path('/path/to/media')
RETENTION_DAYS = 7

def create_backup_dir():
    """Create backup directory if it doesn't exist"""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

def backup_database():
    """Backup SQLite database"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = BACKUP_DIR / f'db_backup_{timestamp}.sqlite3'
    
    try:
        shutil.copy2(DB_NAME, backup_file)
        logging.info(f'Database backup created: {backup_file}')
        return True
    except Exception as e:
        logging.error(f'Database backup failed: {str(e)}')
        return False

def backup_media():
    """Backup media files"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = BACKUP_DIR / f'media_backup_{timestamp}'
    
    try:
        shutil.copytree(MEDIA_DIR, backup_dir)
        logging.info(f'Media backup created: {backup_dir}')
        return True
    except Exception as e:
        logging.error(f'Media backup failed: {str(e)}')
        return False

def cleanup_old_backups():
    """Remove backups older than RETENTION_DAYS"""
    current_time = datetime.now()
    
    for item in BACKUP_DIR.iterdir():
        if item.is_file() or item.is_dir():
            # Get file/directory creation time
            creation_time = datetime.fromtimestamp(item.stat().st_mtime)
            age_days = (current_time - creation_time).days
            
            if age_days > RETENTION_DAYS:
                try:
                    if item.is_file():
                        item.unlink()
                    else:
                        shutil.rmtree(item)
                    logging.info(f'Removed old backup: {item}')
                except Exception as e:
                    logging.error(f'Failed to remove old backup {item}: {str(e)}')

def main():
    """Main backup function"""
    logging.info('Starting backup process')
    
    create_backup_dir()
    
    if backup_database() and backup_media():
        logging.info('Backup completed successfully')
    else:
        logging.error('Backup completed with errors')
    
    cleanup_old_backups()
    logging.info('Backup process finished')

if __name__ == '__main__':
    main() 