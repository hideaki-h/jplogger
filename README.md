# jplogger

python logging wrapper module.  
It wraps logging standard module to be able to use in multi-thread coding and lets you to use logging easily.  
jplogger module includes just one class as log.  
all messages in the module are wirrten as japanese so the module named as jplogger.


# Usage

## import and instaiciate

```
# jploggerを環境変数PYTHONPATHに通すこと
from hideakih_homeunix_net.jplogger import jplogger
# ログクラス生成
log = jplogger(jplogger.debug)
```

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

## now logging works
```
log.log(jplogger.info,'対象ファイルパス: ' + str(file_path.resolve()))
```
```
log.logError('対象ファイルが見つかりません: ' + str(file_path.resolve()))
```

# class method
|method|description|example|
|-|-|-|
|jplogger(jplogger.priority)|constructor to set default log level<br> jplogger.priority as follows: debug,info,notice,warning,error,critical|jplogger(jpllogger.debug)|
|addStdOutHandler(handler)
|log(jplogger.priority, str_msg)|log str_msg as priority <br> jplogger.priority is same as jplogger() |log.log(jplogger.info, 'info msg')|
|logError(¥[str¥]msg)|log ¥[str¥]msg as error|log.logError('error msg')|


# Copyright
It's copyrighted under MIT license.
Just import as you like.

hideakih@nac.homeunix.net
