!#/bin/bash

echo "starting cleanup process..."
find /tmp -name "*.log" -type f -mtime +7 -delete

echo "cleanup finished successfully"
