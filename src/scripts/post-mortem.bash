#!/bin/bash
  set -euo pipefail

  if [[ -z "${GPG_KEY:-}" ]]; then
    echo "Error: GPG_KEY is not set. Please define it as environment variable."
    exit 1
  fi

  FILE=""
  MODE="encrypt"

  START_RE='@notes post-mortem=start'
  END_RE='@notes post-mortem=end'

  usage() {
    echo "Usage: $0 [--encrypt|--decrypt] <file>"
    exit 1
  }

  if [[ $# -eq 1 ]]; then
    FILE="$1"
  elif [[ $# -eq 2 ]]; then
    if [[ "$1" == "--encrypt" || "$1" == "-e" ]]; then
      MODE="encrypt"
    elif [[ "$1" == "--decrypt" || "$1" == "-d" ]]; then
      MODE="decrypt"
    else
      usage
    fi
    FILE="$2"
  else
    usage
  fi

  if [[ ! -f "$FILE" ]]; then
    echo "File not found: $FILE"
    exit 2
  fi

  inside=0
  buffer=()
  output=()

  process_encrypt() {
    local text="$1"
    gpg --encrypt --armor -r "$GPG_KEY" <<< "$text"
  }

  process_decrypt() {
    local text="$1"
    gpg --decrypt --armor -r "$GPG_KEY" <<< "$text"
  }

  while IFS= read -r line || [[ -n "$line" ]]; do
    if [[ "$line" =~ $START_RE ]]; then
      inside=1
      output+=("$line")
      buffer=()
      continue
    fi
    if [[ "$line" =~ $END_RE ]] && [[ $inside -eq 1 ]]; then
      inside=0
      if [[ "$MODE" == "encrypt" ]]; then
        encrypted=$(process_encrypt "$(printf '%s\n' "${buffer[@]}")")
        output+=("$encrypted")
      else
        decrypted=$(process_decrypt "$(printf '%s\n' "${buffer[@]}")")
        output+=("$decrypted")
      fi
      output+=("$line")
      continue
    fi
    if [[ $inside -eq 1 ]]; then
      buffer+=("$line")
    else
      output+=("$line")
    fi
  done < "$FILE"

  printf "%s\n" "${output[@]}" > "$FILE"
