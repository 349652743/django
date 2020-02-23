(function(){
    
})()
$('#btnSelect').click(function(){
    var tmp = $('#contest option:selected').text();
    var conId = tmp.split(':');
    console.log(window.location.href+conId[0]+'/');
    var url = window.location.href.split('/');
    var finalUrl='';
    console.log(url);
    for(var i = 0;i<url.length;i++){
        finalUrl+=url[i]+'/';
        if(url[i]=='detail')break;
    }
    console.log('finalurl:'+finalUrl);
    window.location.href=finalUrl+conId[0]+'/';

});
$('#delConfirm').click(function () {//删除确认
    var rowId = $('#delNid').val();
    console.log(rowId);
    $.ajax({
        url: "/custreg/del_user/",
        type: 'POST',
        data: {'userid': rowId},
        success:function (data) {
            if(data['status']){
                $('tr[nid="'+ rowId+'"]').remove();
            }
            $('#delModal').modal('hide');
        }
    })
        
});
$('#tb').on('click','.del-row',function(){//删除按钮
    $('#delModal').modal('show');
    var rowid = $(this).parent().parent().attr('nid');
    $('#delNid').val(rowid);
});

$('#tb').on('click','.edit-row',function () {//编辑按钮
    $('#eidtModal').modal('show');
    //1.获取当前行的所有数据
    // 将数据赋值到对应的对话框的指定位置
    $(this).parent().prevAll().each(function () {

        var v = $(this).text();
        var n = $(this).attr('na');
    if(n=='department'){
        $("#eidtModal input[name='"+ n +"']").val(v)
    }else if(n=='sex'){
        // v=''
        if(v=='男'){
            $('#eidtModal :radio[value="男"]').prop('checked',true);
        }else{
            $('#eidtModal :radio[value="女"]').prop('checked',true);
        }
    }else {
        // n=stuid
        // v=170511128
        $("#eidtModal input[name='"+ n +"']").val(v)
    }
    });
});
$('#btnEditSave').click(function () {//编辑确认
    var postData = {};
    $('#eidtModal').find('input,select').each(function () {
        var v = $(this).val();
        var n = $(this).attr('name');
        if(n=='sex'){
            if($(this).prop('checked')){
                postData[n] = v;
            }
        }else{
            postData[n] = v;
        }
    });

    $.ajax({
        url: '/custreg/edit_user/',
        type: 'POST',
        data: postData,
        dataType: 'JSON',
        success:function (data) {
            if(data['status']){
                alert('修改成功');
                window.location.reload();
            }else{
                alert('修改失败');
            }
        }
    });
});

$('#addBtn').click(function () {//添加按钮
    $('#addModal').modal('show');
});
$('#btnSave').click(function () {//添加确认
    var postData = {};
    $('#addModal').find('input,select').each(function () {
        var v = $(this).val();
        var n = $(this).attr('name');
        if(n=='sex'){
            if($(this).prop('checked')){
                postData[n] = v;
            }
        }else{
            postData[n] = v;
        }
    });
    //console.log(postData);
    $.ajax({
        url: '/custreg/add_user/',
        type: 'POST',
        data: postData,
        dataType: 'JSON',
        success:function (data) {
            if(data['message']=='添加成功'){
                alert(data['message']);
                window.location.reload();
            }else if(data['message']=='用户已注册,请勿重复添加'){
                alert(data['message']);
            }else{
                alert(data['message']);
            }
        }
    });

});