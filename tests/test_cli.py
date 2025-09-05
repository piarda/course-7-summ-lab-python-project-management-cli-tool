import subprocess

def test_help_command():
    result = subprocess.run(['python3', 'main.py', '--help'], capture_output=True, text=True)
    assert "Project Management CLI Tool" in result.stdout
    assert "add-user" in result.stdout
