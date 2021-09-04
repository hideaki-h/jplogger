# jplogger

python logging wrapper module.  
It wraps logging standard module and lets you use logging easily.  
Multi-logging(handler) with severity supported(SRY. NOW IN DEVELOPPING).  
ex. stdout(notice) and file(info). stdout(info), stderr(warning) and file(debug)  etc...  

jplogger module includes just one class as jplogger.  
all messages in module are wirrten as japanese so the module named as jplogger.  


# Usage

## import and instaiciate with root log level

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

## set hanlder log level

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
|jplogger([jplogger.priority]priority)|constructor to set root log level to priority <br> jplogger.priority as follows: debug,info,notice,warning,error,critical|log = jplogger(jpllogger.debug)|
|addStdOutHandler([string]handler, [jplogger.priority]priority)|add new stdout loghandler as handler with priority to decide to output log by calling log* method as shown below. <br> hanlder is unique name|log.addStdOutHandler('uniquename_for_stdout', jplogger.info)|
|setHandlerLevelByString([string]handler, [string]priority)|set log level of handler specified to priority <br> priority is all upper String  of priority introduced in jplogger()|setHandlerLevelByString('uniqename_for_stdout', 'NOTICE')|
|log([jplogger.priority]priority, [string]msg)|log str_msg as priority <br> jplogger.priority is same as jplogger() |log.log(jplogger.info, 'info msg')|
|logError([string]msg)|log msg as error|log.logError('error msg')|


# Copyright
It's copyrighted under MIT license.
Just import and/or revise as you like and let it contribute your works.

hideakih@nac.homeunix.net
