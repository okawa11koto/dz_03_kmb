while sleep 1; do curl -o /dev/null -s -w "$(date '+%H:%M:%S') %{http_code} %{time_total}s\n" https://s3.mdst.yandex.net/ping; done
