/**
* Created by Edward on 2016/8/20.
*/
$(function(){
    /**
     * Modal 5:意见反馈
     */
    $("#modal5-submit").click(function(){
        //disable editable
        $("#Modal-5 .form-control").prop('disabled',true);
        $("#modal5-submit").prop('disabled',true);

        var url = '/feedback';
        var data = {
            "subject":$("#contact-title").val(),
            "body":$("#contact-content").val(),
        };
        var fnSuccess = function(json){
            $("#Modal-5 .alert").addClass("alert-success").append("<span>邮件已发送成功</span>").alert();
            //enable editable
            $("#Modal-5 .form-control").prop('disabled',false);
            $("#modal5-submit").prop('disabled',false);
        }
        $.ajax({
            url: url,
            contentType: 'application/json;charset=UTF-8',
            type: 'POST',
            dataType: 'json',
            data: JSON.stringify(data),
            success: fnSuccess

        });
    });

});