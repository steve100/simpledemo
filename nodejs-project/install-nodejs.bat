
echo checking node installation
node -v
npm -v

echo "stop here if you get good values"
echo "continue if you want to install a new version of node

pause
echo "pulling a version of node for win11"
curl -O https://nodejs.org/dist/v24.11.0/node-v24.11.0-x64.msi

echo "running the installer"
node-v24.11.0-x64.msi

echo checking node installation
node -v
npm -v
