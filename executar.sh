#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if ! command -v python3 >/dev/null 2>&1; then
  echo 'Erro: Python 3 não encontrado. Instale o Python 3 e tente novamente.' >&2
  exit 1
fi
exec python3 gestor_notas.py
