{{/* Returns the size of Mysql disk */}}
{{- define "quotes.mysql_disk_size" }}
{{- if eq .Values.global.env "prod" }}
      storage: 100Gi
{{- else }}
      storage: 1Gi
{{- end }}
{{- end }}
