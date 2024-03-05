# Define paths for tools
$BLACK_PATH = "build/tools/black"
$PYLINT_PATH = "build/tools/pylint"
$PYTEST_PATH = "build/tools/pytest"

# Create the necessary tool directories if they don't exist
if (-Not (Test-Path $BLACK_PATH)) { New-Item -Path $BLACK_PATH -ItemType Directory -Force }
if (-Not (Test-Path $PYLINT_PATH)) { New-Item -Path $PYLINT_PATH -ItemType Directory -Force }
if (-Not (Test-Path $PYTEST_PATH)) { New-Item -Path $PYTEST_PATH -ItemType Directory -Force }

# Run Black
Write-Host "Running Black..."
$blackResult = black src tests --check 2>&1 | Out-String
$blackResult | Out-File -FilePath "$BLACK_PATH/black_output.txt"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Black found format issues or encountered an error. Check $BLACK_PATH/black_output.txt for details."
    exit 1
}
Write-Host $blackResult

# Run Pylint
Write-Host "Running Pylint..."
$pylintResult = pylint src tests 2>&1 | Out-String
$pylintResult | Out-File -FilePath "$PYLINT_PATH/pylint_output.txt"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pylint encountered issues or errors. Check $PYLINT_PATH/pylint_output.txt for details."
    exit 1
}
Write-Host $pylintResult

# Run Pytest with coverage
Write-Host "Running Pytest with coverage..."
$pytestResult = pytest --cov=src --cov=tests --cov-report=html:"$PYTEST_PATH/htmlcov" --cov-report=xml:"$PYTEST_PATH/coverage.xml" --cov-report=txt:"$PYTEST_PATH/pytest_cov_output.txt" tests 2>&1 | Out-String
$pytestResult | Out-File -FilePath "$PYTEST_PATH/pytest_output.txt"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pytest encountered errors. Check $PYTEST_PATH/pytest_output.txt and $PYTEST_PATH/pytest_cov_output.txt for details."
    exit 1
}
Write-Host $pytestResult
