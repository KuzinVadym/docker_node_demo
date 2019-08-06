'use strict';


module.exports = function(url, form=0, method) {
  if (!method) {
    method = form ? 'POST' : 'GET';
  }
  let uri = url;
  let options = {
    method: method,
    uri: uri,
    headers: { 'Content-Type': 'application/json' },
    json: true,
  };
  if (form) {
    options.body = form;
  }
  return options;
}
