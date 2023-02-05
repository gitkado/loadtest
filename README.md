# 負荷テスト

利用できそうなパッケージを試してみる場

## [locust](https://github.com/locustio/locust)
- [公式ドキュメント](https://docs.locust.io/en/stable/)
- [実行コマンドオプション](https://docs.locust.io/en/stable/config-options.html#)

```shell
$ docker compose -f docker/docker-compose.locust.yml up
```

### レポート例
- `/locust/report/report_exceptions.csv`
  - クライアント側の例外情報
- `/locust/report/report_failures.csv`
  - 失敗したリクエスト情報
- `/locust/report/report_stats.csv`
  - APIごとのリクエスト集計
- `/locust/report/report_stats_history.csv`
  - *The example_history.csv will get new rows with the current (10 seconds sliding window) stats appended during the whole test run.*
  - ↑らしいけどそれっぽい値が出力できなかった...

## [k6](https://github.com/grafana/k6)
- [公式ドキュメント](https://k6.io/docs/)

```shell
$ docker compose -f docker/docker-compose.k6.yml up
```

### レポート例
- `/k6/report/report.csv`
  - APIリクエストごとのメトリクス
- `/k6/report/summary.json`
  - 負荷テスト全体のメトリクス集計
  - `loadtest.js`で`handleSummary()`を書いてないと出力されない
