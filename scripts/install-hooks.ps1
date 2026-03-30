Param(
  [switch]$Force
)

$ErrorActionPreference = 'Stop'

function Backup-IfExists($Path) {
  if (Test-Path $Path) {
    $ts = Get-Date -Format 'yyyyMMddHHmmss'
    Copy-Item -LiteralPath $Path -Destination "$Path.bak-$ts" -Force
  }
}

if (-not (Test-Path .git\hooks)) {
  throw "Error: .git\hooks not found (is this a git repo?)"
}

New-Item -ItemType Directory -Force -Path .git\hooks | Out-Null

$hooks = @('pre-commit', 'post-commit')
foreach ($hook in $hooks) {
  $src = Join-Path '.githooks' $hook
  $dst = Join-Path '.git\hooks' $hook

  if (-not (Test-Path $src)) {
    throw "Error: missing $src"
  }

  if ((Test-Path $dst) -and (-not $Force)) {
    Backup-IfExists $dst
  }

  Copy-Item -LiteralPath $src -Destination $dst -Force
}

Write-Host "Installed git hooks (pre-commit, post-commit)."
