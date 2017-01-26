/**
 * @Descript: 个人头像卡片
 */
$('#user-avatar, #user-avatar-gr').on('click', function(){
    // 浮动窗口定位
    // userfloatPostion();
    // 显示
    $('#com-card-box').show();
    $('.if-shade').css({'opacity' : 0, 'filter' : 'alpha(opacity=50)'}).show();
    $('#user-avatar-hide, .if-shade').click(function(){
        $('#com-card-box').hide();
        $('.if-shade').hide();
    });

});


/**
 *
 * @name 下拉通知菜单
 * @param string 元素ID
 *
 */
mouseGoByDown = function( ele ) {

    var $this = ele;
    var downId = $this+'_menu';
    var downA = $this+'_on';

    $($this).hover(function(){

        $(downA).addClass('on');
        $(downId).removeClass( 'hide' );
        $(downId).addClass( 'show' );

    },function(){

        $(downA).removeClass('on');
        $(downId).removeClass( 'show' );
        $(downId).addClass( 'hide' );

    });

};

/**
 * 个人中心下拉个人头像
 */
mouseGoByDown('#mininav');
