$(document).on('click','#work-page a',function(){
  var page = $(this).attr('href');
  var sub = $('.c-l_c').attr('rel');
      $.ajax({

          type:'post',
          url:'/copylist'+page+'&id='+uid+'&sub='+sub,
          data:1,
          dataType:'json',
          success:function(msg){

              $('#works-list').empty().append(msg.data);
              $('#work-page').empty().append(msg.page);
              $("body").scrollTop(offsetTop);
      return false;
          }

      });
      return false;
  });

//作品分页post
$(document).on('submit','#work-page form',function(){
  var page = parseInt($('#work-page .page_input').val());
  var sub = $('.c-l_c').attr('rel');
  if (isNaN(page)) {
    page = 1;
  }
  $.ajax({

          type:'post',
          url:'/copylist?page='+page+'&id='+uid+'&sub='+sub,
          data:1,
          dataType:'json',
          success:function(msg){

              $('#works-list').empty().append(msg.data);
              $('#work-page').empty().append(msg.page);
              $("body").scrollTop(offsetTop);
      return false;
          }

      });
  return false;
});

//评论分页无刷新
$(document).on('click','#com-p a',function(){
  var page = $(this).attr('href');
      $.ajax({

          type:'post',
          url:'/produclist'+page+'&id='+uid,
          data:1,
          dataType:'json',
          success:function(msg){

              $('#ct-private').empty().append(msg.data);
              $('#com-p').empty().append(msg.cmpage);
              $("body").scrollTop(comTop);
      return false;
          }

      });
      return false;
  });
//评论分页post
$(document).on('submit','#com-p form',function(){
  var page = parseInt($('#com-p .page_input').val());

  if (isNaN(page)) {
    page = 1;
  }
  $.ajax({

          type:'post',
          url:'/produclist?page='+page+'&id='+uid,
          data:1,
          dataType:'json',
          success:function(msg){

              $('#ct-private').empty().append(msg.data);
      $('#com-p').empty().append(msg.cmpage);
      $("body").scrollTop(comTop);
      return false;
          }

      });

  return false;
});

// 全部列表无刷新
$(document).on('click','.c-l a',function(){
  var sub = $(this).attr('rel');
  $.ajax({
          type:'post',
          url:'/copylist?page=1&id='+uid+'&sub='+sub,
          data:1,
          dataType:'json',
          success:function(msg){
            if(msg.data == null){
              $('#us-comment').hide();
              $('#work-page').empty();
              $('#works-list').empty().append('<div class="no-works"></div>');
            }else{
              $('#us-comment').show();
              $('#works-list').empty().append(msg.data);
                $('#work-page').empty().append(msg.page);
            }

              $("body").scrollTop(offsetTop);
      return false;
          }

      });
      return false;

});
