$(document).ready(function () {
    
    let table = new DataTable('#myTable');


    // password show hide

    $('.show_pass').click(function () {
        var x = $(this).siblings('.password_field').attr('type');
        if (x === "password") {
            $(this).siblings('.password_field').attr('type', 'text');
            $(this).find('img').attr('src', 'assets/img/eye.png');
        } else {
            $(this).siblings('.password_field').attr('type', 'password');
            $(this).find('img').attr('src', 'assets/img/eye_off.svg');
        }
    })

    // user dropdown

    $('.user_details .user_name_info .user_type_dropdown .selected_user_type').click(function () {
        $(this).parents('.user_type_dropdown').toggleClass('list_show');
    })


    // sidebar collapse toggle

    $('.frc_dashboard_wrapper .dashboard_wrapper_inner .side_panel .frc_brand_block .menu_trigger').click(function () {
        $(this).parents('.dashboard_wrapper_inner').addClass('sidepanel_hide');
        $(this).hide();
        $('.side_panel .frc_brand_block span.sidebar_show').css('display', 'flex');
    })
    $('.side_panel .frc_brand_block span.sidebar_show').click(function () {
        $('.frc_dashboard_wrapper .dashboard_wrapper_inner').removeClass('sidepanel_hide');
        $(this).hide();
        $('.frc_dashboard_wrapper .dashboard_wrapper_inner .side_panel .frc_brand_block .menu_trigger').show();
    })

    // sort dropdown

    $('.filter_area .filter_sort .sort_dropdown .selected_opt').click(function () {
        $(this).parents('.sort_dropdown').toggleClass('sort_list_show');
    })
    $('.filter_area .filter_sort .sort_dropdown ul.sort_list li').click(function () {
        var sort_txt = $(this).text();
        var sort_val = $(this).attr('data-value');
        $(this).parents('ul.sort_list').siblings('.selected_opt').text(sort_txt);
        $(this).parents('.sort_dropdown').removeClass('sort_list_show');
    })

    // date sort
    $('.date_field input[type=date]').on('change', function () {
        var date = new Date($(this).val());
        var day = date.getDate();
        var month = date.getMonth() + 1;
        var year = date.getFullYear();
        var full_date = day + '/' + month + '/' + year;
        // alert([day, month, year].join('/'));
        // console.log(full_date);
        $(this).siblings('.selected_date').text(full_date);
    })

    // product action,list toggle
    $('.action_block').each(function () {
        $(this).find('.act_btn').click(function () {
            $(this).siblings('.act_list_close').show();
            $(this).siblings('.action_list').addClass('act_list_show');
        })
    })
    $('.act_list_close').click(function () {
        $(this).hide();
        $(this).siblings('.action_list.act_list_show ').removeClass('act_list_show');
    })


    // select dropdown
    $('form .select_group').click(function () {
        $(this).find('.form_field_select').toggleClass('select_show');
    })
    $('form .select_group .form_field_select .select_dropdown li').click(function () {
        $(this).parents('.select_group.select_show').removeClass('select_show');
        var opt_txt = $(this).text();
        $(this).parents('.select_dropdown').siblings('.selected_option').text(opt_txt);

    })

})
