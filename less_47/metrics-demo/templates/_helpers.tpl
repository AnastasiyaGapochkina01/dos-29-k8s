{{- define "app.fullname" -}}
{{- printf "%s-%s" .Release.Name .Values.name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "app.nameWithType" -}}
{{- printf "%s-%s-%s" .Release.Name .Values.name . | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "app.deploymentName" -}}
{{- printf "%s-%s-%s" .Release.Name .Values.name "deployment" | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "app.serviceName" -}}
{{- printf "%s-%s-%s" .Release.Name .Values.name "service" | trunc 63 | trimSuffix "-" -}}
{{- end -}}


