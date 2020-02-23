$('#select').click(function () {
    var number = $('#number').val();
    console.log(number);
    var item = $('input[name=sel_number]:checked').val();
    if(item=='option1'){
        $("#newdiv").empty();
        var html = '<table class="table table-bordered table-striped">'+
                        '<tr id="tr_id">'+
                            '<th>编号</th>'+
                            '<th>姓名</th>'+
                            '<th>年龄</th>'+
                            '<th>性别</th>'+
                            '<th>院系</th>'+
                        '</tr>'+
                        '<tbody id="tb">'+
                        '</tbody>'+
                    '</table>';
        $('#newdiv').append(html);
        $.ajax({
            url: "/Edu/select/",
            type: 'POST',
            data: {'number': number,'option':item},
            success:function (data) {
                //console.log(data['tea_list'][0]['age'])
                for(var i=0;i<data['tea_list'].length;i++){
                    console.log(data['tea_list'][i]['name']);
                    var html2='<tr>'+
                        '<td na="number">'+data['tea_list'][i]['number']+'</td>'+
                        '<td na="name">'+data['tea_list'][i]['name']+'</td>'+
                        '<td na="sex">'+data['tea_list'][i]['sex']+'</td>'+
                        '<td na="age">'+data['tea_list'][i]['age']+'</td>'+
                        '<td na="department">'+data['tea_list'][i]['department']+'</td>'+
                    '</tr>';
                    $('#tb').append(html2);
                }
            }
        })
    }else if(item=='option2'){
        $("#newdiv").empty();
        var html = '<table class="table table-bordered table-striped">'+
                        '<tr id="tr_id">'+
                            '<th>课程编号</th>'+
                            '<th>教师编号</th>'+
                            '<th>教师姓名</th>'+
                            '<th>开始时间</th>'+
                            '<th>结束时间</th>'+
                            '<th>日期</th>'+
                        '</tr>'+
                        '<tbody id="tb">'+
                        '</tbody>'+
                    '</table>';
        $('#newdiv').append(html);
        $.ajax({
            url: "/Edu/select/",
            type: 'POST',
            data: {'number': number,'option':item},
            success:function (data) {
                //console.log(data['tea_list'][0]['age'])
                for(var i=0;i<data['cla_list'].length;i++){
                    // console.log(data['cla_list'][i]['name']);
                    var html2='<tr>'+
                        '<td na="number">'+data['cla_list'][i]['number']+'</td>'+
                        '<td na="name">'+data['cla_list'][i]['use_statime']+'</td>'+
                        '<td na="sex">'+data['cla_list'][i]['use_endtime']+'</td>'+
                        '<td na="age">'+data['cla_list'][i]['use_course']+'</td>'+
                        '<td na="department">'+data['cla_list'][i]['use_teacher']+'</td>'+
                        '<td na="department">'+data['cla_list'][i]['use_date']+'</td>'+
                    '</tr>';
                    $('#tb').append(html2);
                }
            }
        })
    }else{
        $("#newDiv").empty();
        var html = '<table class="table table-bordered table-striped">'+
                        '<tr id="tr_id">'+
                            '<th>教室编号</th>'+
                            '<th>占用开始时间</th>'+
                            '<th>占用结束时间</th>'+
                            '<th>课程编号</th>'+
                            '<th>教师编号</th>'+
                            '<th>占用日期</th>'+
                        '</tr>'+
                        '<tbody id="tb">'+
                        '</tbody>'+
                    '</table>';
        $('#newdiv').append(html);
        $.ajax({
            url: "/Edu/select/",
            type: 'POST',
            data: {'number': number,'option':item},
            success:function (data) {
                //console.log(data['tea_list'][0]['age'])
                for(var i=0;i<data['cou_list'].length;i++){
                    //console.log(data['tea_list'][i]['name']);
                    var html2='<tr>'+
                        '<td na="number">'+data['cou_list'][i]['number']+'</td>'+
                        '<td na="name">'+data['cou_list'][i]['tea_number']+'</td>'+
                        '<td na="sex">'+data['cou_list'][i]['tea_name']+'</td>'+
                        '<td na="age">'+data['cou_list'][i]['sta_time']+'</td>'+
                        '<td na="department">'+data['cou_list'][i]['end_time']+'</td>'+
                        '<td na="department">'+data['cou_list'][i]['date']+'</td>'+
                    '</tr>';
                    $('#tb').append(html2);
                }
            }
        })
    }
    
    //console.log(item);
    
        
});