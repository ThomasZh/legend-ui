
var page = function(pag ,pos ,req, url) {
	var urlParams = '';
	for (var i in url) {
		if (url[i] == null) {
			urlParams += "&"+i+"="+getPar(i);
		} else {
			urlParams += "&"+i+"="+url[i];
		}
	}
	$(pag+' a').not('#on').click(function() {
		$(pos).load(req+$(this).attr('href')+urlParams);
		$(document).scrollTop(0);
		return false;
	});
	$(pag+' li form').submit(function() {
		var page = parseInt($(pag+' li form input[type="text"]').val());
		if (isNaN(page)) {
			page = 1;
		}
		$(pos).load(req+'?page='+page+urlParams);
		return false;
	});
};
function getPar(par){
    //获取当前URL
    var local_url = document.location.href;
    //获取要取得的get参数位置
    var get = local_url.indexOf(par +"=");
    if(get == -1){
        return false;
    }
    //截取字符串
    var get_par = local_url.slice(par.length + get + 1);
    //判断截取后的字符串是否还有其他get参数
    var nextPar = get_par.indexOf("&");
    if(nextPar != -1){
        get_par = get_par.slice(0, nextPar);
	}
	return get_par;
}
