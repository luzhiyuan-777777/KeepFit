/**
 * Created by luzhiyuan on 2018/1/2.
 */

function isNull(data,message) {
        if (data == null || data == undefined || data == ''){
            alert(message);
            return false;
        }else {
            return true;
        }
    }