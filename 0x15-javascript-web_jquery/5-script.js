$('DIV#add_item').click(() => {
	var newItem = $('<li>Item</li>');
	$('UL.my_list').append(newItem);
});
