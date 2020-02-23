$('.radio').on('click','#see_answer',function(){
    console.log($(this).siblings('.title').text());
    $(this).siblings('.title').text($(this).parent().attr('nid')+'.'+$(this).parent().attr('title')+'答案：'+$(this).parent().attr('answer'));
});
$('.radio').on('click','#add_wrong',function(){
    var data ={};
    data['title']=[];
    data['title'].push($(this).parent().attr('title'));
    console.log(data['title']);
    $.ajax({
        url: '/question/add_wrong/',
        type: 'POST',
        data: data,
        traditional:true,
        dataType: 'JSON',
        success:function (data) {
            if(data['message']=='添加成功'){
                alert(data['message']);
            }
        }
    });
});
$('.radio').on('click','#erase_wrong',function(){
    var data ={};
    data['title']=[];
    data['title'].push($(this).parent().attr('title'));
    console.log(data['title']);
    $.ajax({
        url: '/question/erase_wrong/',
        type: 'POST',
        data: data,
        traditional:true,
        dataType: 'JSON',
        success:function (data) {
            if(data['message']=='删除成功'){
                alert(data['message']);
            }
        }
    });
});
$('.checkbox').on('click','#see_answer',function(){
    console.log($(this).parent().attr('answer'));
    $(this).siblings('.title').text($(this).parent().attr('nid')+'.'+$(this).parent().attr('title')+'答案：'+$(this).parent().attr('answer'));
});
$('.checkbox').on('click','#add_wrong',function(){
    var data ={};
    data['title']=[];
    data['title'].push($(this).parent().attr('title'));
    console.log(data['title']);
    $.ajax({
        url: '/question/add_wrong/',
        type: 'POST',
        data: data,
        traditional:true,
        dataType: 'JSON',
        success:function (data) {
            if(data['message']=='添加成功'){
                alert(data['message']);
            }
        }
    });
});
$('.checkbox').on('click','#erase_wrong',function(){
    var data ={};
    data['title']=[];
    data['title'].push($(this).parent().attr('title'));
    console.log(data['title']);
    $.ajax({
        url: '/question/erase_wrong/',
        type: 'POST',
        data: data,
        traditional:true,
        dataType: 'JSON',
        success:function (data) {
            if(data['message']=='删除成功'){
                alert(data['message']);
            }
        }
    });
});
$('#submit').click(function(){
    var score=0;
    $('.radio').each(function(){
        var answer = $(this).attr('answer');
        var choice = $("input[name="+$(this).attr('nid')+"Radios]:checked").val();
        $(this).find('.title').text($(this).attr('nid')+'.'+$(this).attr('title')+'答案：'+$(this).attr('answer'));
        // console.log('option'+answer);
        // console.log(choice);
        if('option'+answer==choice){
            score+=1;
        }else {
            $(this).find('.title').css("color","red");
        }
    });
    $('.checkbox').each(function(){
        var chk_value = [];//定义一个数组    
        $('input[name='+$(this).attr('nid')+'checkbox]:checked').each(function(){//遍历每一个名字为interest的复选框，其中选中的执行函数    
            chk_value.push($(this).val());//将选中的值添加到数组chk_value中    
        });
        $(this).find('.title').text($(this).attr('nid')+'.'+$(this).attr('title')+'答案：'+$(this).attr('answer'));
        // console.log($(this).attr('answer'));
        var str = $(this).attr('answer');
        if(str!=undefined)
        var ans_value = str.split(',');
        console.log(ans_value);
        console.log(chk_value);
        var flag=1;
        for(var i=0;i<ans_value.length;i++){
            if('option'+ans_value[i]!=chk_value[i])flag=0;
            console.log('option'+ans_value[i]);
            console.log(chk_value[i]);
        }
        if(flag==0||ans_value.length!=chk_value.length){
            $(this).find('.title').css("color","red");
        }else {
            score+=1;
        }
    });
    alert('总分:'+score);
});
$('#reload').click(function(){
    window.location.reload();
});
