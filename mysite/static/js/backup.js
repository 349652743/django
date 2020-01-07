$('#backup_btn').on('click',function(){
    $('#backupModal').modal('show');
});
$('#recovery_btn').on('click',function(){
    $('#recoveryModal').modal('show');
});
$('#backupConfirm').on('click',function(){
    $.ajax({
        url: "/Edu/backup/",
        type: 'POST',
        data: {'option': 1},
        success:function (data) {
            if(data['message']=="备份成功"){
                $('#backupModal').modal('hide');
            }
            alert(data['message']);
        }
    })
    
});
$('#recoveryConfirm').on('click',function(){
    $.ajax({
        url: "/Edu/backup/",
        type: 'POST',
        data: {'option': 2},
        success:function (data) { 
            if(data['message']=="恢复成功"){
                $('#recoveryModal').modal('hide');
            }
            alert(data['message']);
        }
    })
});