#$NewPath = "C:\sqlite3"

# will want to revisit for a generic script
# This sets a default to the newpath if one is not passed into the script

param(
    [string]$NewPath = "C:\sqlite3"
)


$OldPath = [Environment]::GetEnvironmentVariable("Path", "Machine")

# Only add if not already in PATH
if ($OldPath -notlike "*$NewPath*") {
    $NewPathValue = $OldPath + ";" + $NewPath
    [Environment]::SetEnvironmentVariable("Path", $NewPathValue, "Machine")
    Write-Host "Added to system PATH."
} else {
    Write-Host "Path already exists."
}

Write-Host "Remember to close the command window and reopen to pickup the new path"
Write-Host "Sleep 5"
sleep 5
