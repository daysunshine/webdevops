$(function () {
    function check(choice) {
                if (choice == 0) {
                    var hostname = $('#c_hostname').val().length;
                    var ip = $('#c_address').val().length;
                    var c_location = $('#c_location').val().length;
                    var hosttype = $('#c_host_type').val().length;
                    var memory = $('#c_memory').val().length;
                    var v_cpu = $('#c_cpu_v').val().length;
                    var n_cpu = $('#c_cpu_num').val().length;
                    var c_os = $('#c_os').val().length;
                    var c_status = $('#c_status').val().length;
                    if (hostname!=0 && ip!=0 && c_location!=0 && hosttype!=0 && memory!=0 && v_cpu!=0 && n_cpu!=0 && c_os!=0 && c_status!=0){
                        $("input[id=add_button]").attr("disabled", false);
                    };
                }if (choice == 1) {
                    var hostname = $('#u_hostname').val().length;
                    var ip = $('#u_address').val().length;
                    var c_location = $('#u_location').val().length;
                    var hosttype = $('#u_host_type').val().length;
                    var memory = $('#u_memory').val().length;
                    var v_cpu = $('#u_cpu_v').val().length;
                    var n_cpu = $('#u_cpu_num').val().length;
                    var c_os = $('#u_os').val().length;
                    var c_status = $('#u_status').val().length;
                    if (hostname!=0 && ip!=0 && c_location!=0 && hosttype!=0 && memory!=0 && v_cpu!=0 && n_cpu!=0 && c_os!=0 && c_status!=0){
                        $("input[id=update_button]").attr("disabled", false);
                    };
                }
        }
    // myModal_create 模态框关闭后清除表单数据
    $('#myModal_create').on('hidden.bs.modal', function (){
        document.getElementById("add-form").reset();
    });
    // create new host msg
    $('#add_button').click(function () {
        if($("input[id=add_button]").attr("disabled") != "disabled"){
            var data = {};
            var data_form = $('#add-form').serializeArray();
            $.each(data_form, function () {
                data[this.name] = this.value;
            });
            var token = $('input[name=csrfmiddlewaretoken]').val();
            data.csrfmiddlewaretoken = token;
            $.ajax({
                type:"POST",
                // url:"{% url 'app:addhost' %}",
                url:"/app/addhost/",
                dataType: 'json',
                data:data,
                success:function (e) {
                    $('#myModal_create').modal('hide')
                    if (e.error == 0) {
                        $('#mytable').bootstrapTable("refresh")
                        var addhost = bootbox.dialog({
                            title: "添加成功",
                            message: "<p><i class='glyphicon glyphicon-ok-sign'></i>"+e.message+"</p>",
                            size: 'small',
                            closeButton: false,
                            onEscape: true,
                            callback:function () {}
                        });
                        addhost.init(function(){
                            setTimeout(function(){
                                addhost.modal('hide');
                            }, 1000);
                        });
                    }else{
                        var addhost = bootbox.dialog({
                            title:"添加失败",
                            message: "<p><i class='glyphicon glyphicon-remove-sign'></i>"+e.message+"</p>",
                            size: 'small',
                            closeButton: false,
                            onEscape: true,
                            callback:function () {}
                        });
                        addhost.init(function(){
                            setTimeout(function(){
                                addhost.modal('hide');
                            }, 1000);
                        });
                    }
                }
            });
        }else {
            bootbox.alert({
                message:"<div style='color:red'>请将信息填写完整!</div>",
                size:"small",
            });
        }
    });
    // update host msg
    $('#update_button').click(function () {
        if($("input[id=update_button]").attr("disabled") != "disabled"){
            var data = {};
            var data_form = $('#update-form').serializeArray();
            $.each(data_form, function () {
                data[this.name] = this.value;
            });
            var token = $('input[name=csrfmiddlewaretoken]').val();
            data.csrfmiddlewaretoken = token;
            $.ajax({
                type:"POST",
                // url:"{% url 'app:updatehost' %}",
                url:"/app/updatehost/",
                dataType: 'json',
                data:data,
                success:function (e) {
                    $('#myModal_update').modal('hide')
                    if (e.error == 0) {
                        $('#mytable').bootstrapTable("refresh")
                        var addhost = bootbox.dialog({
                            title: "更新成功",
                            message: "<p><i class='glyphicon glyphicon-ok-sign'></i>"+e.message+"</p>",
                            size: 'small',
                            closeButton: false,
                            onEscape: true,
                            callback:function () {}
                        });
                        addhost.init(function(){
                            setTimeout(function(){
                                addhost.modal('hide');
                            }, 1000);
                        });
                    }else{
                        var addhost = bootbox.dialog({
                            title:"更新失败",
                            message: "<p><i class='glyphicon glyphicon-remove-sign'></i>"+e.message+"</p>",
                            size: 'small',
                            closeButton: false,
                            onEscape: true,
                            callback:function () {}
                        });
                        addhost.init(function(){
                            setTimeout(function(){
                                addhost.modal('hide');
                            }, 1000);
                        });
                    }
                }
            });
        }else {
            bootbox.alert({
                message:"<div style='color:red'>请将信息填写完整!</div>",
                size:"small",
            });
        }
    });

    // 验证输入信息 create
    $('#myModal_create').on('shown.bs.modal', function () {
        $("input[id=add_button]").attr("disabled", true);
        $('#c_hostname').blur(function () {
           if ($('#c_hostname').val().length == 0){
               $('.c_hostname_error').html('主机名不能为空').show();
           }else{
               $('.c_hostname_error').hide();
           };
           check(0);
        });
        $('#c_address').blur(function () {
           <!-- 检测输入ip合法性 -->
           var exp=/^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
           if ($('#c_address').val().match(exp) == null){
               $('.c_address_error').html('IP地址不能为空').show();
           }else{
               $('.c_address_error').hide();
           };
           check(0);
        });
        $('#c_location').blur(function () {
           if ($('#c_location').val().length == 0){
               $('.c_location_error').html('请选择主机位置').show();
           }else{
               $('.c_location_error').hide();
           };
           check(0);
        });
        $('#c_host_type').blur(function () {
           if ($('#c_host_type').val().length == 0){
               $('.c_host_type_error').html('请选择主机类型').show();
           }else{
               $('.c_host_type_error').hide();
           };
           check(0);
        });
        $('#c_memory').blur(function () {
           var exp=/^([1-9]+\d*)$/;
           if ($('#c_memory').val().length == 0) {
               $('.c_memory_error').html('主机内存不能为空').show();
           }else{
               if ($('#c_memory').val().match(exp) == null){
                   $('.c_memory_error').html('主机内存不能为小数或浮点数').show();
               }else{
                   $('.c_memory_error').hide();
               }
           };
           check(0);
        });
        $('#c_cpu_v').blur(function () {
           if ($('#c_cpu_v').val().length == 0){
               $('.c_cpu_v_error').html('CPU型号不能为空').show();
           }else{
               $('.c_cpu_v_error').hide();
           };
           check(0);
        });
        $('#c_cpu_num').blur(function () {
           var exp=/^([1-9]+\d*)$/;
           if ($('#c_cpu_num').val().length == 0) {
               $('.c_cpu_num_error').html('CPU线程数不能为空').show();
           }else{
               if ($('#c_cpu_num').val().match(exp) == null){
                   $('.c_cpu_num_error').html('CPU线程数不能为小数或浮点数').show();
               }else{
                   $('.c_cpu_num_error').hide();
               }
           };
            check(0);
        });
        $('#c_os').blur(function () {
           if ($('#c_os').val().length == 0){
               $('.c_os_error').html('请选择操作系统类型').show();
           }else{
               $('.c_os_error').hide();
           };
           check(0);
        });
        $('#c_status').blur(function () {
           if ($('#c_status').val().length == 0){
               $('.c_status_error').html('请选择主机运行状态').show();
           }else{
               $('.c_status_error').hide();
           }
           check(0);
        });

    });
    // 验证输入信息 update
    $('#myModal_update').on('shown.bs.modal', function () {
            $("input[id=update_button]").attr("disabled", true);
            $('#u_hostname').blur(function () {
               if ($('#c_hostname').val().length == 0){
                   $('.c_hostname_error').html('主机名不能为空').show();
               }else{
                   $('.c_hostname_error').hide();
               };
               check(1);
            });
            $('#u_address').blur(function () {
               <!-- 检测输入ip合法性 -->
               var exp=/^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$/;
               if ($('#c_address').val().match(exp) == null){
                   $('.c_address_error').html('IP地址不能为空').show();
               }else{
                   $('.c_address_error').hide();
               };
               check(1);
            });
            $('#u_location').blur(function () {
               if ($('#c_location').val().length == 0){
                   $('.c_location_error').html('请选择主机位置').show();
               }else{
                   $('.c_location_error').hide();
               };
               check(1);
            });
            $('#u_host_type').blur(function () {
               if ($('#c_host_type').val().length == 0){
                   $('.c_host_type_error').html('请选择主机类型').show();
               }else{
                   $('.c_host_type_error').hide();
               };
               check(1);
            });
            $('#u_memory').blur(function () {
               var exp=/^([1-9]+\d*)$/;
               if ($('#c_memory').val().length == 0) {
                   $('.c_memory_error').html('主机内存不能为空').show();
               }else{
                   if ($('#c_memory').val().match(exp) == null){
                       $('.c_memory_error').html('主机内存不能为小数或浮点数').show();
                   }else{
                       $('.c_memory_error').hide();
                   }
               };
               check(1);
            });
            $('#u_cpu_v').blur(function () {
               if ($('#c_cpu_v').val().length == 0){
                   $('.c_cpu_v_error').html('CPU型号不能为空').show();
               }else{
                   $('.c_cpu_v_error').hide();
               };
               check(1);
            });
            $('#u_cpu_num').blur(function () {
               var exp=/^([1-9]+\d*)$/;
               if ($('#c_cpu_num').val().length == 0) {
                   $('.c_cpu_num_error').html('CPU线程数不能为空').show();
               }else{
                   if ($('#c_cpu_num').val().match(exp) == null){
                       $('.c_cpu_num_error').html('CPU线程数不能为小数或浮点数').show();
                   }else{
                       $('.c_cpu_num_error').hide();
                   }
               };
                check(1);
            });
            $('#u_os').blur(function () {
               if ($('#c_os').val().length == 0){
                   $('.c_os_error').html('请选择操作系统类型').show();
               }else{
                   $('.c_os_error').hide();
               };
               check(1);
            });
            $('#u_status').blur(function () {
               if ($('#c_status').val().length == 0){
                   $('.c_status_error').html('请选择主机运行状态').show();
               }else{
                   $('.c_status_error').hide();
               }
               check(1);
            });
        });

    $('#btn_delete').click(function () {
        var rows = $("#mytable").bootstrapTable('getSelections');// 获得要删除的数据
        if (rows.length == 0) {
            bootbox.alert({
                message:"<div style='color:red'>请选择要删除的主机!</div>",
                size:"small",
            });
            return;
        }else {
            var ids = new Array();// 声明一个数组
            $(rows).each(function() {// 通过获得被选中的来进行遍历
                ids.push(this.id);// cid为获得到的整条数据中的一列
            });
            delHost(ids)
        }
    });

    function delHost(ids) {
        bootbox.confirm({
        title:"批量删除",
        message:"<div style='color:red'>确定删除吗?</div>",
        callback:function (result) {
            if(result){
                var data = "";
                csrf = $("input[name='csrfmiddlewaretoken']").val();
                if (ids.length == 1) {
                    data = "ids="+ids+","+"&"+"csrfmiddlewaretoken="+csrf
                }else{
                    data = "ids="+ids+"&"+"csrfmiddlewaretoken="+csrf
                }
                $.ajax({
                    type:"POST",
                    dataType:"json",
                    url:"/app/delhost/",
                    data:data,
                    success: function(e){
                        if (e.error == 0) {
                            $('#mytable').bootstrapTable("refresh")
                            var dialog = bootbox.dialog({
                                title: "批量删除成功",
                                message: "<p><i class='glyphicon glyphicon-ok-sign'></i>"+e.message+"</p>",
                                size: 'small',
                                closeButton: false,
                                onEscape: true,
                                callback:function () {}
                            });
                            dialog.init(function(){
                                setTimeout(function(){
                                    dialog.modal('hide');
                                }, 1000);
                            });
                        }else{
                            var dialog = bootbox.dialog({
                                title: "批量删除失败",
                                message: "<p><i class='glyphicon glyphicon-remove-sign'></i>"+e.message+"</p>",
                                size: 'small',
                                closeButton: false,
                                onEscape: true,
                                callback:function () {}
                            });
                            dialog.init(function(){
                                setTimeout(function(){
                                    dialog.modal('hide');
                                }, 1000);
                            });
                        }
                    },
                });
            };
        }, <!-- callback end-->
    }); <!-- confirm end-->
    };

})




