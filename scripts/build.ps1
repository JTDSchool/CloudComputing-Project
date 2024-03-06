. .\venv\Scripts\Activate.ps1

$BLACK_PATH = "build\tools\black"
$PYLINT_PATH = "build\tools\pylint"
$PYTEST_PATH = "build\tools\pytest"

New-Item -Path $BLACK_PATH -ItemType Directory -Force
New-Item -Path $PYLINT_PATH -ItemType Directory -Force
New-Item -Path $PYTEST_PATH -ItemType Directory -Force

Write-Host " "
Write-Host "--------- BLACK ---------------------------"
Write-Host " "
$blackCommand = black src tests --config pyproject.toml --verbose 2>&1
$blackOutput = $blackCommand | Tee-Object -FilePath "$BLACK_PATH\black_output.txt"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Black found format issues or encountered an error."
    exit 1
}

Write-Host " "
Write-Host "--------- PYLINT ---------------------------"
Write-Host " "
$pylintCommand = pylint --rcfile pyproject.toml src tests --verbose 2>&1
$pylintOutput = $pylintCommand | Tee-Object -FilePath "$PYLINT_PATH\pylint_output.txt"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pylint encountered issues or errors."
    exit 1
}

Write-Host " "
Write-Host "--------- PYTEST /W COVERAGE ---------------------------"
Write-Host " "
$pytestCommand = pytest 2>&1
$pytestOutput = $pytestCommand | Tee-Object -FilePath "$PYTEST_PATH\pytest_output.txt"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pytest encountered errors."
    exit 1
}

deactivate

