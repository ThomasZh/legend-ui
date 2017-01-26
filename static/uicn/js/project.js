//延迟加载
$(document).ready(function(){
      $('.imgloadinglater').lazyload({
          threshold : -100, //距离100像素触发
          effect : "fadeIn" //显示特效
      });
  });



  /**
 * 评论鼠标经过
 */
$(document).on('mouseenter', '#ct-private li', function(event){
  $(this).find('.ct-bottom a').show();
  event.stopPropagation();
});
$(document).on('mouseleave', '#ct-private li', function(event){
  $(this).find('.ct-bottom a').hide();
  event.stopPropagation();
});



// 回复留言
$(document).on('click', '.myreplay', function(){
  var _rel = $(this).attr('_rel');
  var rel = $(this).attr('rel');

  myReplayId = rel;

  var myReplayName = $('#replay_'+_rel).find('.ct-user a').text();
  var replayString = '@'+myReplayName+':  ';

  $('textarea[name=replycont]').focus().val(replayString);

});

/**
 *
 * @name 评论
 * @param string 元素ID
 *
 */
textAreaFocus = function( ele ) {
  var eleVal = $('textarea[name='+ele+']').text();
  var $this = $('textarea[name='+ele+']');
  $(document).on('focus', 'textarea[name='+ele+']', function(){
    $(this).addClass('blur');
    if ( $this.val() == eleVal ){
      $(this).val('');
    }
  })
  $(document).on('blur', 'textarea[name='+ele+']', function(){
    $(this).removeClass('blur');
    if( $this.val() == '' ){
      $(this).val(eleVal);
    }

  })

};

/**
 * 评论
 */
textAreaFocus('replycont');

// 留言
var replyDefVal = $('textarea[name=replycont]').text();
$('#submit-mess').click(function(){
  if(!sid){
    globalTip({'msg':'登录后才能评论!','setTime':3,'jump':true,'URL':'http://ui.cn/login.html'});
    return false;
  }else{

    $(this).addClass('loading');
    $(this).text('');
    $(this).attr('disabled',true);

    var $this = $('textarea[name=replycont]');
    var newReplyDefVal = $('textarea[name=replycont]').val();

    if ( newReplyDefVal == replyDefVal || $this == newReplyDefVal || $this == '' || newReplyDefVal == '') {

      $('#submit-mess').removeClass('loading');
      $('#submit-mess').text('留言');
      $('#submit-mess').removeAttr('disabled');
      globalTip({'msg':'留言内容不能为空!','setTime':3});
      $this.focus();
      return false;
    };

    if ( myReplayId != 0 ) {

      // 将中文冒号换成英文冒号
      newReplyDefVal = newReplyDefVal.replace('：', ':');
      var replayRep = /^@.*?:/

      // 匹配出@用户名
      var atName = newReplyDefVal.match(replayRep);

      // 如果匹配为空时
      if ( atName == null ) {

        myReplayId = 0;

      }

      newReplyDefVal = newReplyDefVal.replace(atName, '');
      newReplyDefVal = newReplyDefVal.trim();

    };

    var replyData = {

      atc			:	'msg',
      msgid		:	myReplayId,		//回复得评论者ID
      sid  		:   sid,	//登录得用户ID
      uid			:	uid,	//用户中心ID
      replycont	:	newReplyDefVal,
      token		:   token

    };

    $.ajax({
      type:'post',
      dataType:'json',
      url:'/add',
      data:replyData,
      success:function(data){
        if(data.code == '1'){
          globalTip(data);
          $('#user-liu').text(200);
          $('#submit-mess').removeClass('loading');
          $('#submit-mess').text('留言');
          $('#submit-mess').removeAttr('disabled');
          var replayHtml;
            replayHtml  = '<li id="replay_'+data.comid+'" class="replay-bg">';
            replayHtml += '<a href="user.php?id='+data.userid+'" class="us-ava">';
            replayHtml += '<img class="us-ava-img" src="'+data.head+'" />';
            replayHtml += '</a>';
            replayHtml += '<div class="ct-box">';
            replayHtml += '<p class="ct-user">';
            replayHtml += '<a href="user.php?id='+data.userid+'">'+data.username+'</a> :';
            replayHtml += '</p>';
            replayHtml += '<p class="ct-reply">';

            if ( data.replyto != 0 && data.replyto == myReplayId) {

              replayHtml += '<a href="user.php?id='+data.replyto+'">@'+data.replyname+'</a> : ';

            };
            replayHtml += data.content;

            replayHtml += '</p>';
            replayHtml += '<p class="ct-bottom"><span>'+data.time+'</span><a class="replaydel" href="javascript:;" _rel="'+data.comid+'">删除</a></p>';
            replayHtml += '</div>';
            replayHtml += '</li>';

          $('#ct-private').prepend(replayHtml).slideDown();

          // 加载评论内容
          $.ajax({

                  type:'post',
                  url:'/produclist?page=1&id='+uid,
                  data:1,
                  dataType:'json',
                  success:function(msg){

                      $('#ct-private').empty().append(msg.data);
                      $('#com-p').empty().append(msg.cmpage);
                      // $("body").scrollTop(455);
              return false;
                  }

              });

          $this.val(replyDefVal);
        }
        else{
          $('#submit-mess').removeClass('loading');
          $('#submit-mess').text('留言');
          $('#submit-mess').removeAttr('disabled');
          globalTip(data);
        }
      }
    });


    return false;
  }

});


// 删除留言
$(document).on('click', '.replaydel', function(){
  var _rel = $(this).attr('_rel');
  var rel = $(this).attr('rel');
  var replayDelData = {
    atc			:	'msg',
    ct			:	'del',
    sid			:	 sid,	//是否是登录下的用户ID，才可以删除
    msgid		:	_rel,	//评论的ID
    uid 		:   rel
  };

  $.ajax({
    type:'post',
    dataType:'json',
    url:'/del',
    data:replayDelData,
    success:function(data){
      if(data.code == '1'){
        globalTip(data);
        $('#replay_'+data.msgid).slideUp('slow', function(){
          $(this).remove();
          // 加载评论内容
        });
        // 加载评论内容
        $.ajax({

                type:'post',
                url:'/produclist?page=1&id='+uid,
                data:1,
                dataType:'json',
                success:function(msg){

                    $('#ct-private').empty().append(msg.data);
                    $('#com-p').empty().append(msg.cmpage);
            return false;
                }

            });

      }else{

        globalTip(data);
      }
    }
  });

  return false;

});


// 关注
$('#follow').click(function(){

  if(!sid){
    globalTip({'msg':'登录后才能关注!','setTime':3,'jump':true,'URL':'http://ui.cn/login.html'});
    return false;

  }else{

    var ct,
      data = $(this).attr('data'),
      $this = $('#follow'),
      fansNum = parseInt( $('#user-fans strong').text() );
    // 关注状态
    if ( data == 'follow' ) {
      ct = 'add';
    }
    // 取消关注
    if ( data == 'unfollow' ) {
      ct = 'del';
    };

    var followData = {
      act		:	'follow',
      ct		:	ct,
      followid:	uid,	//被关注ID
      uid     :   sid 	//关注ID
    };

    if ( data == 'follow' ) {	// 关注
      $.ajax({
        type:'post',
        dataType:'json',
        url:'/follow',
        data:followData,
        success:function(data){
          if ( data.code == '1' ) {

            // ta 关注俺了吗?
            if( data.isfollow != '2' ){
              $this.removeClass('myfollow');
              $this.addClass('havefollow');
              $this.attr('_rel', 'havefollow');

              $this.find('strong').text('已关注');
            }else{
              $this.removeClass('myfollow');
              $this.addClass('mutualfollow');
              $this.attr('_rel', 'mutualfollow');

              $this.find('strong').text('相互关注');
            }

            $this.attr('data', 'unfollow');
            fansNum = fansNum + 1;
            $('#user-fans strong').text( fansNum );

          }
        }

      });

    }

    if ( data == 'unfollow' ) {	// 取消关注
      $.ajax({
        type:'post',
        dataType:'json',
        url:'/follow',
        data:followData,
        success:function(data){
          if ( data.code == '1' ) {
            $this.removeClass('havefollow');
            $this.removeClass('mutualfollow');
            $this.removeClass('unfollow');

            $this.addClass('myfollow');
            $this.find('strong').text('关 注');

            $this.attr('data', 'follow');
            $this.attr('_rel', 'follow');
            fansNum = fansNum - 1;
            if(fansNum < 0){
              fansNum = 0;
            }
            $('#user-fans strong').text( fansNum );

          }
        }

      });

    }
    return false;
  }
});

// 关注鼠标经过

$('.follow-icon').hover(function(){
  var _rel = $(this).attr('_rel');
  if ( _rel == 'havefollow' ) { 	//已关注
    $(this).removeClass('havefollow');
    $(this).addClass('unfollow');
    $(this).find('strong').text('取消关注');
  }else if ( _rel == 'mutualfollow' ) {	// 相互关注
    $(this).removeClass('mutualfollow');
    $(this).addClass('unfollow');
    $(this).find('strong').text('取消关注');
  }else if ( _rel == 'follow') {
    $(this).addClass('onfollow');
  }
},function(){
  var _rel = $(this).attr('_rel');
  if ( _rel == 'havefollow' ) { 	//已关注
    $(this).removeClass('unfollow');
    $(this).addClass('havefollow');
    $(this).find('strong').text('已关注');
  }else if ( _rel == 'mutualfollow' ) {	// 相互关注
    $(this).removeClass('unfollow');
    $(this).addClass('mutualfollow');
    $(this).find('strong').text('相互关注');
  }else if ( _rel == 'follow') {
    $(this).removeClass('onfollow');
  }
});

/**
 * @Descript: 私信窗口浮动层定位方法函数
 * @Author	: LangLee
 */
userfloatPostion = function(){
  //获取改变之后的宽度
  var changeWidth=$(window).width();
  var changeHeight=$(window).height();
  // 获取DIV宽度
  var smallW = $('#com-backs-box').width();
  var smallH = $('#com-backs-box').height();
  //计算宽度修改比例
  var divChangeWidth	=	(changeWidth - smallW) / 2;
  var divChangeHeight	=	(changeHeight - smallH) / 2;
  $('#com-backs-box').css('top', divChangeHeight);
  $('#com-backs-box').css('left', divChangeWidth);
};

// 私信
$('#private-letters').on('click', function(){

  if(!sid){
    globalTip({'msg':'登录后才能发私信!','setTime':3,'jump':true,'URL':'http://ui.cn/login.html'});
    return false;
  }else{
    // 浮动窗口定位
    userfloatPostion();

    // 显示
    $('#com-backs-box').show();
    $('.if-shade').show();

    // 窗口调整时位置变化
    $(window).resize(function(){
      // 浮动窗口定位
      userfloatPostion();
    });

    $('.private-text').focus();

    // 点击关闭按钮以及遮罩层时关闭浮动层
    $('.mini-button-close, .if-shade').bind('click', function(){
      $('#com-backs-box').hide();
      $('.if-shade').hide();
      $('textarea[name=lettersval]').val('');
    });
  }

});


// 头部公共部分发送私信
$('#letters-submit').on('click', function(){

  var contentVal = $('textarea[name=lettersval]').val();

  if ( contentVal == '' ) {
    globalTip({'msg':'内容不能为空!','setTime':3});
    $('textarea[name=lettersval]').focus();
    return false;
  }

  if(contentVal.length >= 200){
    globalTip({'msg':'内容不能超过200字!','setTime':3});
    $('textarea[name=lettersval]').focus();
    return false;
  }

  var lettersData = {
    fromid		:	sid,
    toid		:	uid,
    content		:	contentVal,
    token		:   token
  };

  $.ajax({
        type:'post',
        url:'/letterSend',
        data:lettersData,
        dataType:'json',
        success:function(data){

            if(data.code == 1){
                globalTip({'msg':'私信发送成功!','setTime':3});
        $('#com-backs-box').hide();
        $('.if-shade').hide();

        $('textarea[name=lettersval]').val('');
            }else{
                globalTip(data);

            }
        }
      })

  return false;
});

//点击标签
$(".c-l").each(function(i){
  $(".c-l").eq(i).find("a").click(function(){
    $('.c-l').find('a').removeClass('c-l_c');
    $(this).addClass('c-l_c');
    if(i == 1){	//如果点击原创时，外层li添加属性d 值为1与分享区分
      $(".c-l").eq(1).attr("d","1");
      $(".c-l").eq(2).attr("d","2");
      $(".c-l").eq(1).addClass("c-l-hover")
      $(".c-l").eq(1).find('ul li').show();
    }else if(i == 2){	//如果点击分享时，外层li添加属性d 值为2与原创区分
      $(".c-l").eq(2).attr("d","1");
      $(".c-l").eq(1).attr("d","2");
      $(".c-l").eq(2).addClass("c-l-hover")
      $(".c-l").eq(2).find('ul li').show();
    }else{	//点击全部或者临摹时
      $(this).parents(".c-l").siblings(".c-l").removeClass("c-l-hover").removeAttr("d");
      $(this).parents(".c-l").siblings(".c-l").find("ul").hide();
    }
  });
});

// 鼠标划入分享
$('.c-l').eq(2).mousemove(function(){
  $('.c-l').eq(1).find('ul').hide();
  $('.c-l').eq(1).removeClass('c-l-hover');

  $(this).find('ul').show();
  $(this).addClass('c-l-hover');
});

// 鼠标划入原创
$('.c-l').eq(1).mousemove(function(){

  $('.c-l').eq(2).find('ul').hide();
  $('.c-l').eq(2).removeClass('c-l-hover');

  $(this).find('ul').show();
  $(this).addClass('c-l-hover');
});

// 鼠标离开分享
$('.c-l').eq(2).mouseleave(function(){
  var td = $(this).attr("d");

  if(td == 1){
    $(this).find('ul').show();
    $(this).addClass('c-l-hover');
    $(".c-l").eq(1).removeClass("c-l-hover");
    $(".c-l").eq(1).find("ul").hide();
  }else if(td == 2){
    $(".c-l").eq(1).addClass("c-l-hover");
    $(".c-l").eq(1).find("ul").show();
    $(this).find('ul').hide();
    $(this).removeClass('c-l-hover');
  }else{
    $(this).find('ul').hide();
    $(this).removeClass('c-l-hover');
  }
});


// 鼠标离开原创时
$('.c-l').eq(1).mouseleave(function(){
  var td = $(this).attr("d");

  if(td == 1){
    $(this).find('ul').show();
    $(this).addClass('c-l-hover');
    $(".c-l").eq(2).removeClass("c-l-hover");
    $(".c-l").eq(2).find("ul").hide();
  }else if(td == 2){
    $(".c-l").eq(2).addClass("c-l-hover");
    $(".c-l").eq(2).find("ul").show();
    $(this).find('ul').hide();
    $(this).removeClass('c-l-hover');
  }else{
    $(this).find('ul').hide();
    $(this).removeClass('c-l-hover');
  }

});
