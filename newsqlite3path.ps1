$NewPath = "C:\sqlite3"
$OldPath = [Environment]::GetEnvironmentVariable("Path", "Machine")

# Only add if not already in PATH
if ($OldPath -notlike "*$NewPath*") {
    $NewPathValue = $OldPath + ";" + $NewPath
    [Environment]::SetEnvironmentVariable("Path", $NewPathValue, "Machine")
    Write-Host "Added to system PATH."
} else {
    Write-Host "Path already exists."
}
