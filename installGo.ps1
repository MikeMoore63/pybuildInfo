# Install the current Go release
param(
	[string]$w='',
	[string]$v='1.21.1'
)

# installer file
$file = 'go' + $v + '.windows-amd64.msi'

# set defaults
$workDir = 'Documents\go'
$url = 'https://dl.google.com/go/' + $file
$dest = Join-Path $Home "Downloads"
$dest = Join-Path $dest $file

# if $w wasn't passed; use the default
if ($w -eq "") {
    $gopath = Join-Path $Home $workDir
} else {
    $gopath = $w
}

# Setup the Go workspace; if it doesn't exist.
If (!(Test-Path $gopath)) {
    New-Item -path $gopath -type directory
}

# Create GOPATH and set PATH to use $GOPATH\bin
$gopathbin = Join-Path $gopath "bin"
#$gopathbin = ';' + $gopathbin

# set the $GOPATH
[Environment]::SetEnvironmentVariable( "GOPATH", $gopath, [System.EnvironmentVariableTarget]::User )

# see the $GOBIN
[Environment]::SetEnvironmentVariable( "GOBIN", $gopathbin, [System.EnvironmentVariableTarget]::User )

Write-Output "downloading $url"
# Create client, set its info, and download
$wc = New-Object System.Net.WebClient
$wc.UseDefaultCredentials = $true
$wc.Headers.Add("X-FORMS_BASED_AUTH_ACCEPTED", "f")
$wc.DownloadFile($url, $dest)

Write-Output "$url downloaded as $dest"
Write-Output "installing $v..."
# Run the msi
Start-Process $dest

Write-Output "done"

#
#
# $url = 'https://dl.google.com/go/go1.21.1.windows-amd64.zip';
# Write-Host ('Downloading {0} ...' -f $url);
# [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;
# Invoke-WebRequest -Uri $url -OutFile 'go.zip';
# Write-Host 'Expanding ...'; 	Expand-Archive go.zip -DestinationPath C:\\;
# Write-Host 'Moving ...';
# Move-Item -Path C:\\go -Destination 'C:\\Program Files\\Go'