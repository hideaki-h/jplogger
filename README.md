# introduction of jplogger

python logging wrapper module.  
It wraps logging standard module and lets you use logging easily.  
Multi-logging(handler) with severity supported(SRY. NOW IN DEVELOPPING).  
ex. stdout(notice) and file(info). stdout(info), stderr(warning) and file(debug)  etc...  

jplogger module includes just one class of "jplogger".  
all messages in module are wirrten as japanese so the module named as jplogger.  


# Usage

## import and instaiciate with root-level log level

```
# jploggerを環境変数PYTHONPATHに通すこと
from hideakih_homeunix_net.jplogger import jplogger
# ログクラス生成
log = jplogger(jplogger.debug)
```

## set output handler

### for stdout
```
# 標準出力ログハンドラー追加
log.addStdOutHandler('stdout', jplogger.debug)
```
### for file(IN DEVELOP)
```
N/A
```

## change hanlder-base log level if you needs

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
|jplogger([jplogger.priority]priority)|constructor to set root-base log level to priority. <br> jplogger.priority as follows: debug,info,notice,warning,error,critical|log = jplogger(jpllogger.debug)|
|addStdOutHandler([string]HANDLER, [jplogger.priority]PRIORITY)|add new stdout loghandler as HANDLER with hanlder-base PRIORITY to decide to output log by calling log* method as shown below. <br> HANDLER: unique name to specify the handler|log.addStdOutHandler('uniquename_for_stdout', jplogger.info)|
|setHandlerLevelByString([string]HANDLER, [string]PRIORITY)|set handler-base log level of HANDLER specified to PRIORITY <br> PRIORITY: all upper case string of priority introduced in jplogger()|setHandlerLevelByString('uniqename_for_stdout', 'NOTICE')|
|log([jplogger.priority]PRIORITY, [string]MSG)|log MSG as PRIORITY.|log.log(jplogger.info, 'info msg')|
|logCritical([string]MSG)|log MSG as critical.|log.logCritical('critical msg')|
|logError([string]MSG)|log MSG as error.|log.logError('error msg')|
|logWarning([string]MSG)|log MSG as warning.|log.logWarning('warning msg')|
|logNotice([string]MSG)|log MSG as notice.|log.logNotice('notice msg')|
|logInfo([string]MSG)|log MSG as info.|log.logInfo('info msg')|
|logDebug([string]MSG)|log MSG as debug.|log.logDebug('debug msg')|


# Copyright
It's copyrighted under MIT license.  
Just import and/or revise as you like and let it contribute your works.  

hideakih@nac.homeunix.net
