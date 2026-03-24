#!/bin/bash

echo "cleaning up /tmp logs..."
find /tmp -name "*.log" -type f -mtime +7 -delete
echo "cleanup complete"