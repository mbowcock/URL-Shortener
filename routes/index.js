
exports.index = function(req, res){
  /*res.render('index', { title: 'Express' })*/
  var id = req.params.id;

  /* if id passed then parse from base36 */
  if(id){
	var url = parseInt(id, 36);
	res.send(id + " " + url);
  } else {
	  res.send("No url sent");
  }
};
