# jplogger

pythonログライブラリ

# Usage

## import

import as log

## set output handler

```
# 標準出力ログハンドラー追加
log.addStdOutHandler('stdout', jplogger.debug)
```

## set log level

```
# ログレベル設定
if os.environ.get('LOG_LEVEL') is not None:
	log.setHandlerLevelByString('stdout', os.environ.get('LOG_LEVEL'))
```
```
```

## new logging works
```
log.log(jplogger.info,'対象ファイルパス: ' + str(file_path.resolve()))
```
```
log.logError('対象ファイルが見つかりません: ' + str(file_path.resolve()))
```

# class method
|method|description|example|
|-|-|-|
|log(jplogger.priority, str)|log str as priority <br> jplogger.priority as follows: debug,info,notice,warning,error|log.log(jplogger.info, 'info msg'|
|logError(str)|log str as error|log.logError('error msg')|

