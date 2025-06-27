#!/usr/bin/env python3
"""
Script to build PyWRFKit documentation.
"""

import os
import sys
import subprocess
import shutil

def main():
    """Build the documentation."""
    print("Building PyWRFKit documentation...")
    
    # Change to docs directory
    docs_dir = os.path.join(os.path.dirname(__file__), 'docs')
    os.chdir(docs_dir)
    
    # Clean previous build
    if os.path.exists('_build'):
        print("Cleaning previous build...")
        shutil.rmtree('_build')
    
    # Build documentation
    print("Building HTML documentation...")
    result = subprocess.run(['make', 'html'], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Documentation built successfully!")
        print(f"📁 Documentation available at: {os.path.abspath('_build/html/index.html')}")
    else:
        print("❌ Documentation build failed!")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 