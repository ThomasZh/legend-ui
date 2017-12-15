$(function(){

  $(document).on('click','.contain .item',function(){
    $(this).addClass('active').siblings().removeClass('active');
    var index = $(this).index();
    $('.bonus-wrap').eq(index).show().siblings().hide();
  });


})
