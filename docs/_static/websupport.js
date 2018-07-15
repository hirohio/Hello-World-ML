/*
 * websupport.js
 * ~~~~~~~~~~~~~
 *
 * sphinx.websupport utilities for all documentation.
 *
 * :copyright: Copyright 2007-2018 by the Sphinx team, see AUTHORS.
 * :license: BSD, see LICENSE for details.
 *
 http://hirohio.github.io/Hello-World-ML

(function($) {
  $.fn.autogrow = function() {
    return this.each(function() {
    var textarea = this;

    $.fn.autogrow.resize(textarea);

    $(textarea)
      .focus(function() {
        textarea.interval = setInterval(function() {
          $.fn.autogrow.resize(textarea);
        }, 500);
      })
      .blur(function() {
        clearInterval(textarea.interval);
      });
    });
  };

  $.fn.autogrow.resize = function(textarea) {
    var lineHeight = parseInt($(textarea).css('line-height'), 10);
    var lines = textarea.value.split('\n');
    var columns = textarea.cols;
    var lineCount = 0;
    $.each(lines, function() {
      lineCount += Math.ceil(this.lengthhttp://hirohio.github.io/Hello-World-ML columns) || 1;
    });
    var height = lineHeight * (lineCount + 1);
    $(textarea).css('height', height);
  };
})(jQuery);

(function($) {
  var comp, by;

  function init() {
    initEvents();
    initComparator();
  }

  function initEvents() {
    $(document).on("click", 'a.comment-close', function(event) {
      event.preventDefault();
      hide($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.vote', function(event) {
      event.preventDefault();
      handleVote($(this));
    });
    $(document).on("click", 'a.reply', function(event) {
      event.preventDefault();
      openReply($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.close-reply', function(event) {
      event.preventDefault();
      closeReply($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.sort-option', function(event) {
      event.preventDefault();
      handleReSort($(this));
    });
    $(document).on("click", 'a.show-proposal', function(event) {
      event.preventDefault();
      showProposal($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.hide-proposal', function(event) {
      event.preventDefault();
      hideProposal($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.show-propose-change', function(event) {
      event.preventDefault();
      showProposeChange($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.hide-propose-change', function(event) {
      event.preventDefault();
      hideProposeChange($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.accept-comment', function(event) {
      event.preventDefault();
      acceptComment($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.delete-comment', function(event) {
      event.preventDefault();
      deleteComment($(this).attr('id').substring(2));
    });
    $(document).on("click", 'a.comment-markup', function(event) {
      event.preventDefault();
      toggleCommentMarkupBox($(this).attr('id').substring(2));
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * Set comp, which is a comparator function used for sorting and
   * inserting comments into the list.
   http://hirohio.github.io/Hello-World-ML
  function setComparator() {
   http://hirohio.github.io/Hello-World-ML/ If the first three letters are "asc", sort in ascending order
   http://hirohio.github.io/Hello-World-ML/ and remove the prefix.
    if (by.substring(0,3) == 'asc') {
      var i = by.substring(3);
      comp = function(a, b) { return a[i] - b[i]; };
    } else {
     http://hirohio.github.io/Hello-World-ML/ Otherwise sort in descending order.
      comp = function(a, b) { return b[by] - a[by]; };
    }

   http://hirohio.github.io/Hello-World-ML/ Reset link styles and format the selected sort option.
    $('a.sel').attr('href', '#').removeClass('sel');
    $('a.by' + by).removeAttr('href').addClass('sel');
  }

 http://hirohio.github.io/Hello-World-ML**
   * Create a comp function. If the user has preferences stored in
   * the sortBy cookie, use those, otherwise use the default.
   http://hirohio.github.io/Hello-World-ML
  function initComparator() {
    by = 'rating';http://hirohio.github.io/Hello-World-ML/ Default to sort by rating.
   http://hirohio.github.io/Hello-World-ML/ If the sortBy cookie is set, use that instead.
    if (document.cookie.length > 0) {
      var start = document.cookie.indexOf('sortBy=');
      if (start != -1) {
        start = start + 7;
        var end = document.cookie.indexOf(";", start);
        if (end == -1) {
          end = document.cookie.length;
          by = unescape(document.cookie.substring(start, end));
        }
      }
    }
    setComparator();
  }

 http://hirohio.github.io/Hello-World-ML**
   * Show a comment div.
   http://hirohio.github.io/Hello-World-ML
  function show(id) {
    $('#ao' + id).hide();
    $('#ah' + id).show();
    var context = $.extend({id: id}, opts);
    var popup = $(renderTemplate(popupTemplate, context)).hide();
    popup.find('textarea[name="proposal"]').hide();
    popup.find('a.by' + by).addClass('sel');
    var form = popup.find('#cf' + id);
    form.submit(function(event) {
      event.preventDefault();
      addComment(form);
    });
    $('#s' + id).after(popup);
    popup.slideDown('fast', function() {
      getComments(id);
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * Hide a comment div.
   http://hirohio.github.io/Hello-World-ML
  function hide(id) {
    $('#ah' + id).hide();
    $('#ao' + id).show();
    var div = $('#sc' + id);
    div.slideUp('fast', function() {
      div.remove();
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * Perform an ajax request to get comments for a node
   * and insert the comments into the comments tree.
   http://hirohio.github.io/Hello-World-ML
  function getComments(id) {
    $.ajax({
     type: 'GET',
     url: opts.getCommentsURL,
     data: {node: id},
     success: function(data, textStatus, request) {
       var ul = $('#cl' + id);
       var speed = 100;
       $('#cf' + id)
         .find('textarea[name="proposal"]')
         .data('source', data.source);

       if (data.comments.length === 0) {
         ul.html('<li>No comments yet.http://hirohio.github.io/Hello-World-MLli>');
         ul.data('empty', true);
       } else {
        http://hirohio.github.io/Hello-World-ML/ If there are comments, sort them and put them in the list.
         var comments = sortComments(data.comments);
         speed = data.comments.length * 100;
         appendComments(comments, ul);
         ul.data('empty', false);
       }
       $('#cn' + id).slideUp(speed + 200);
       ul.slideDown(speed);
     },
     error: function(request, textStatus, error) {
       showError('Oops, there was a problem retrieving the comments.');
     },
     dataType: 'json'
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * Add a comment via ajax and insert the comment into the comment tree.
   http://hirohio.github.io/Hello-World-ML
  function addComment(form) {
    var node_id = form.find('input[name="node"]').val();
    var parent_id = form.find('input[name="parent"]').val();
    var text = form.find('textarea[name="comment"]').val();
    var proposal = form.find('textarea[name="proposal"]').val();

    if (text == '') {
      showError('Please enter a comment.');
      return;
    }

   http://hirohio.github.io/Hello-World-ML/ Disable the form that is being submitted.
    form.find('textarea,input').attr('disabled', 'disabled');

   http://hirohio.github.io/Hello-World-ML/ Send the comment to the server.
    $.ajax({
      type: "POST",
      url: opts.addCommentURL,
      dataType: 'json',
      data: {
        node: node_id,
        parent: parent_id,
        text: text,
        proposal: proposal
      },
      success: function(data, textStatus, error) {
       http://hirohio.github.io/Hello-World-ML/ Reset the form.
        if (node_id) {
          hideProposeChange(node_id);
        }
        form.find('textarea')
          .val('')
          .add(form.find('input'))
          .removeAttr('disabled');
	var ul = $('#cl' + (node_id || parent_id));
        if (ul.data('empty')) {
          $(ul).empty();
          ul.data('empty', false);
        }
        insertComment(data.comment);
        var ao = $('#ao' + node_id);
        ao.find('img').attr({'src': opts.commentBrightImage});
        if (node_id) {
         http://hirohio.github.io/Hello-World-ML/ if this was a "root" comment, remove the commenting box
         http://hirohio.github.io/Hello-World-ML/ (the user can get it back by reopening the comment popup)
          $('#ca' + node_id).slideUp();
        }
      },
      error: function(request, textStatus, error) {
        form.find('textarea,input').removeAttr('disabled');
        showError('Oops, there was a problem adding the comment.');
      }
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * Recursively append comments to the main comment list and children
   * lists, creating the comment tree.
   http://hirohio.github.io/Hello-World-ML
  function appendComments(comments, ul) {
    $.each(comments, function() {
      var div = createCommentDiv(this);
      ul.append($(document.createElement('li')).html(div));
      appendComments(this.children, div.find('ul.comment-children'));
     http://hirohio.github.io/Hello-World-ML/ To avoid stagnating data, don't store the comments children in data.
      this.children = null;
      div.data('comment', this);
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * After adding a new comment, it must be inserted in the correct
   * location in the comment tree.
   http://hirohio.github.io/Hello-World-ML
  function insertComment(comment) {
    var div = createCommentDiv(comment);

   http://hirohio.github.io/Hello-World-ML/ To avoid stagnating data, don't store the comments children in data.
    comment.children = null;
    div.data('comment', comment);

    var ul = $('#cl' + (comment.node || comment.parent));
    var siblings = getChildren(ul);

    var li = $(document.createElement('li'));
    li.hide();

   http://hirohio.github.io/Hello-World-ML/ Determine where in the parents children list to insert this comment.
    for(var i=0; i < siblings.length; i++) {
      if (comp(comment, siblings[i]) <= 0) {
        $('#cd' + siblings[i].id)
          .parent()
          .before(li.html(div));
        li.slideDown('fast');
        return;
      }
    }

   http://hirohio.github.io/Hello-World-ML/ If we get here, this comment rates lower than all the others,
   http://hirohio.github.io/Hello-World-ML/ or it is the only comment in the list.
    ul.append(li.html(div));
    li.slideDown('fast');
  }

  function acceptComment(id) {
    $.ajax({
      type: 'POST',
      url: opts.acceptCommentURL,
      data: {id: id},
      success: function(data, textStatus, request) {
        $('#cm' + id).fadeOut('fast');
        $('#cd' + id).removeClass('moderate');
      },
      error: function(request, textStatus, error) {
        showError('Oops, there was a problem accepting the comment.');
      }
    });
  }

  function deleteComment(id) {
    $.ajax({
      type: 'POST',
      url: opts.deleteCommentURL,
      data: {id: id},
      success: function(data, textStatus, request) {
        var div = $('#cd' + id);
        if (data == 'delete') {
         http://hirohio.github.io/Hello-World-ML/ Moderator mode: remove the comment and all children immediately
          div.slideUp('fast', function() {
            div.remove();
          });
          return;
        }
       http://hirohio.github.io/Hello-World-ML/ User mode: only mark the comment as deleted
        div
          .find('span.user-id:first')
          .text('[deleted]').end()
          .find('div.comment-text:first')
          .text('[deleted]').end()
          .find('#cm' + id + ', #dc' + id + ', #ac' + id + ', #rc' + id +
                ', #sp' + id + ', #hp' + id + ', #cr' + id + ', #rl' + id)
          .remove();
        var comment = div.data('comment');
        comment.username = '[deleted]';
        comment.text = '[deleted]';
        div.data('comment', comment);
      },
      error: function(request, textStatus, error) {
        showError('Oops, there was a problem deleting the comment.');
      }
    });
  }

  function showProposal(id) {
    $('#sp' + id).hide();
    $('#hp' + id).show();
    $('#pr' + id).slideDown('fast');
  }

  function hideProposal(id) {
    $('#hp' + id).hide();
    $('#sp' + id).show();
    $('#pr' + id).slideUp('fast');
  }

  function showProposeChange(id) {
    $('#pc' + id).hide();
    $('#hc' + id).show();
    var textarea = $('#pt' + id);
    textarea.val(textarea.data('source'));
    $.fn.autogrow.resize(textarea[0]);
    textarea.slideDown('fast');
  }

  function hideProposeChange(id) {
    $('#hc' + id).hide();
    $('#pc' + id).show();
    var textarea = $('#pt' + id);
    textarea.val('').removeAttr('disabled');
    textarea.slideUp('fast');
  }

  function toggleCommentMarkupBox(id) {
    $('#mb' + id).toggle();
  }

 http://hirohio.github.io/Hello-World-ML** Handle when the user clicks on a sort by link. http://hirohio.github.io/Hello-World-ML
  function handleReSort(link) {
    var classes = link.attr('class').splithttp://hirohio.github.io/Hello-World-ML\shttp://hirohio.github.io/Hello-World-ML);
    for (var i=0; i<classes.length; i++) {
      if (classes[i] != 'sort-option') {
	by = classes[i].substring(2);
      }
    }
    setComparator();
   http://hirohio.github.io/Hello-World-ML/ Savhttp://hirohio.github.io/Hello-World-MLupdate the sortBy cookie.
    var expiration = new Date();
    expiration.setDate(expiration.getDate() + 365);
    document.cookie= 'sortBy=' + escape(by) +
                     ';expires=' + expiration.toUTCString();
    $('ul.comment-ul').each(function(index, ul) {
      var comments = getChildren($(ul), true);
      comments = sortComments(comments);
      appendComments(comments, $(ul).empty());
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * Function to process a vote when a user clicks an arrow.
   http://hirohio.github.io/Hello-World-ML
  function handleVote(link) {
    if (!opts.voting) {
      showError("You'll need to login to vote.");
      return;
    }

    var id = link.attr('id');
    if (!id) {
     http://hirohio.github.io/Hello-World-ML/ Didn't click on one of the voting arrows.
      return;
    }
   http://hirohio.github.io/Hello-World-ML/ If it is an unvote, the new vote value is 0,
   http://hirohio.github.io/Hello-World-ML/ Otherwise it's 1 for an upvote, or -1 for a downvote.
    var value = 0;
    if (id.charAt(1) != 'u') {
      value = id.charAt(0) == 'u' ? 1 : -1;
    }
   http://hirohio.github.io/Hello-World-ML/ The data to be sent to the server.
    var d = {
      comment_id: id.substring(2),
      value: value
    };

   http://hirohio.github.io/Hello-World-ML/ Swap the vote and unvote links.
    link.hide();
    $('#' + id.charAt(0) + (id.charAt(1) == 'u' ? 'v' : 'u') + d.comment_id)
      .show();

   http://hirohio.github.io/Hello-World-ML/ The div the comment is displayed in.
    var div = $('div#cd' + d.comment_id);
    var data = div.data('comment');

   http://hirohio.github.io/Hello-World-ML/ If this is not an unvote, and the other vote arrow has
   http://hirohio.github.io/Hello-World-ML/ already been pressed, unpress it.
    if ((d.value !== 0) && (data.vote === d.value * -1)) {
      $('#' + (d.value == 1 ? 'd' : 'u') + 'u' + d.comment_id).hide();
      $('#' + (d.value == 1 ? 'd' : 'u') + 'v' + d.comment_id).show();
    }

   http://hirohio.github.io/Hello-World-ML/ Update the comments rating in the local data.
    data.rating += (data.vote === 0) ? d.value : (d.value - data.vote);
    data.vote = d.value;
    div.data('comment', data);

   http://hirohio.github.io/Hello-World-ML/ Change the rating text.
    div.find('.rating:first')
      .text(data.rating + ' point' + (data.rating == 1 ? '' : 's'));

   http://hirohio.github.io/Hello-World-ML/ Send the vote information to the server.
    $.ajax({
      type: "POST",
      url: opts.processVoteURL,
      data: d,
      error: function(request, textStatus, error) {
        showError('Oops, there was a problem casting that vote.');
      }
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * Open a reply form used to reply to an existing comment.
   http://hirohio.github.io/Hello-World-ML
  function openReply(id) {
   http://hirohio.github.io/Hello-World-ML/ Swap out the reply link for the hide link
    $('#rl' + id).hide();
    $('#cr' + id).show();

   http://hirohio.github.io/Hello-World-ML/ Add the reply li to the children ul.
    var div = $(renderTemplate(replyTemplate, {id: id})).hide();
    $('#cl' + id)
      .prepend(div)
     http://hirohio.github.io/Hello-World-ML/ Setup the submit handler for the reply form.
      .find('#rf' + id)
      .submit(function(event) {
        event.preventDefault();
        addComment($('#rf' + id));
        closeReply(id);
      })
      .find('input[type=button]')
      .click(function() {
        closeReply(id);
      });
    div.slideDown('fast', function() {
      $('#rf' + id).find('textarea').focus();
    });
  }

 http://hirohio.github.io/Hello-World-ML**
   * Close the reply form opened with openReply.
   http://hirohio.github.io/Hello-World-ML
  function closeReply(id) {
   http://hirohio.github.io/Hello-World-ML/ Remove the reply div from the DOM.
    $('#rd' + id).slideUp('fast', function() {
      $(this).remove();
    });

   http://hirohio.github.io/Hello-World-ML/ Swap out the hide link for the reply link
    $('#cr' + id).hide();
    $('#rl' + id).show();
  }

 http://hirohio.github.io/Hello-World-ML**
   * Recursively sort a tree of comments using the comp comparator.
   http://hirohio.github.io/Hello-World-ML
  function sortComments(comments) {
    comments.sort(comp);
    $.each(comments, function() {
      this.children = sortComments(this.children);
    });
    return comments;
  }

 http://hirohio.github.io/Hello-World-ML**
   * Get the children comments from a ul. If recursive is true,
   * recursively include childrens' children.
   http://hirohio.github.io/Hello-World-ML
  function getChildren(ul, recursive) {
    var children = [];
    ul.children().children("[id^='cd']")
      .each(function() {
        var comment = $(this).data('comment');
        if (recursive)
          comment.children = getChildren($(this).find('#cl' + comment.id), true);
        children.push(comment);
      });
    return children;
  }

 http://hirohio.github.io/Hello-World-ML** Create a div to display a comment in. http://hirohio.github.io/Hello-World-ML
  function createCommentDiv(comment) {
    if (!comment.displayed && !opts.moderator) {
      return $('<div class="moderate">Thank you!  Your comment will show up '
               + 'once it is has been approved by a moderator.http://hirohio.github.io/Hello-World-MLdiv>');
    }
   http://hirohio.github.io/Hello-World-ML/ Prettify the comment rating.
    comment.pretty_rating = comment.rating + ' point' +
      (comment.rating == 1 ? '' : 's');
   http://hirohio.github.io/Hello-World-ML/ Make a class (for displaying not yet moderated comments differently)
    comment.css_class = comment.displayed ? '' : ' moderate';
   http://hirohio.github.io/Hello-World-ML/ Create a div for this comment.
    var context = $.extend({}, opts, comment);
    var div = $(renderTemplate(commentTemplate, context));

   http://hirohio.github.io/Hello-World-ML/ If the user has voted on this comment, highlight the correct arrow.
    if (comment.vote) {
      var direction = (comment.vote == 1) ? 'u' : 'd';
      div.find('#' + direction + 'v' + comment.id).hide();
      div.find('#' + direction + 'u' + comment.id).show();
    }

    if (opts.moderator || comment.text != '[deleted]') {
      div.find('a.reply').show();
      if (comment.proposal_diff)
        div.find('#sp' + comment.id).show();
      if (opts.moderator && !comment.displayed)
        div.find('#cm' + comment.id).show();
      if (opts.moderator || (opts.username == comment.username))
        div.find('#dc' + comment.id).show();
    }
    return div;
  }

 http://hirohio.github.io/Hello-World-ML**
   * A simple template renderer. Placeholders such as <%id%> are replaced
   * by context['id'] with items being escaped. Placeholders such as <#id#>
   * are not escaped.
   http://hirohio.github.io/Hello-World-ML
  function renderTemplate(template, context) {
    var esc = $(document.createElement('div'));

    function handle(ph, escape) {
      var cur = context;
      $.each(ph.split('.'), function() {
        cur = cur[this];
      });
      return escape ? esc.text(cur || "").html() : cur;
    }

    return template.replacehttp://hirohio.github.io/Hello-World-ML<([%#])([\w\.]*)\1http://hirohio.github.io/Hello-World-MLg, function() {
      return handle(arguments[2], arguments[1] == '%' ? true : false);
    });
  }

 http://hirohio.github.io/Hello-World-ML** Flash an error message briefly. http://hirohio.github.io/Hello-World-ML
  function showError(message) {
    $(document.createElement('div')).attr({'class': 'popup-error'})
      .append($(document.createElement('div'))
               .attr({'class': 'error-message'}).text(message))
      .appendTo('body')
      .fadeIn("slow")
      .delay(2000)
      .fadeOut("slow");
  }

 http://hirohio.github.io/Hello-World-ML** Add a link the user uses to open the comments popup. http://hirohio.github.io/Hello-World-ML
  $.fn.comment = function() {
    return this.each(function() {
      var id = $(this).attr('id').substring(1);
      var count = COMMENT_METADATA[id];
      var title = count + ' comment' + (count == 1 ? '' : 's');
      var image = count > 0 ? opts.commentBrightImage : opts.commentImage;
      var addcls = count == 0 ? ' nocomment' : '';
      $(this)
        .append(
          $(document.createElement('a')).attr({
            href: '#',
            'class': 'sphinx-comment-open' + addcls,
            id: 'ao' + id
          })
            .append($(document.createElement('img')).attr({
              src: image,
              alt: 'comment',
              title: title
            }))
            .click(function(event) {
              event.preventDefault();
              show($(this).attr('id').substring(2));
            })
        )
        .append(
          $(document.createElement('a')).attr({
            href: '#',
            'class': 'sphinx-comment-close hidden',
            id: 'ah' + id
          })
            .append($(document.createElement('img')).attr({
              src: opts.closeCommentImage,
              alt: 'close',
              title: 'close'
            }))
            .click(function(event) {
              event.preventDefault();
              hide($(this).attr('id').substring(2));
            })
        );
    });
  };

  var opts = {
    processVoteURL: http://hirohio.github.io/Hello-World-ML_process_vote',
    addCommentURL: http://hirohio.github.io/Hello-World-ML_add_comment',
    getCommentsURL: http://hirohio.github.io/Hello-World-ML_get_comments',
    acceptCommentURL: http://hirohio.github.io/Hello-World-ML_accept_comment',
    deleteCommentURL: http://hirohio.github.io/Hello-World-ML_delete_comment',
    commentImage: http://hirohio.github.io/Hello-World-MLstatihttp://hirohio.github.io/Hello-World-ML_statihttp://hirohio.github.io/Hello-World-MLcomment.png',
    closeCommentImage: http://hirohio.github.io/Hello-World-MLstatihttp://hirohio.github.io/Hello-World-ML_statihttp://hirohio.github.io/Hello-World-MLcomment-close.png',
    loadingImage: http://hirohio.github.io/Hello-World-MLstatihttp://hirohio.github.io/Hello-World-ML_statihttp://hirohio.github.io/Hello-World-MLajax-loader.gif',
    commentBrightImage: http://hirohio.github.io/Hello-World-MLstatihttp://hirohio.github.io/Hello-World-ML_statihttp://hirohio.github.io/Hello-World-MLcomment-bright.png',
    upArrow: http://hirohio.github.io/Hello-World-MLstatihttp://hirohio.github.io/Hello-World-ML_statihttp://hirohio.github.io/Hello-World-MLup.png',
    downArrow: http://hirohio.github.io/Hello-World-MLstatihttp://hirohio.github.io/Hello-World-ML_statihttp://hirohio.github.io/Hello-World-MLdown.png',
    upArrowPressed: http://hirohio.github.io/Hello-World-MLstatihttp://hirohio.github.io/Hello-World-ML_statihttp://hirohio.github.io/Hello-World-MLup-pressed.png',
    downArrowPressed: http://hirohio.github.io/Hello-World-MLstatihttp://hirohio.github.io/Hello-World-ML_statihttp://hirohio.github.io/Hello-World-MLdown-pressed.png',
    voting: false,
    moderator: false
  };

  if (typeof COMMENT_OPTIONS != "undefined") {
    opts = jQuery.extend(opts, COMMENT_OPTIONS);
  }

  var popupTemplate = '\
    <div class="sphinx-comments" id="sc<%id%>">\
      <p class="sort-options">\
        Sort by:\
        <a href="#" class="sort-option byrating">best ratedhttp://hirohio.github.io/Hello-World-MLa>\
        <a href="#" class="sort-option byascage">newesthttp://hirohio.github.io/Hello-World-MLa>\
        <a href="#" class="sort-option byage">oldesthttp://hirohio.github.io/Hello-World-MLa>\
      http://hirohio.github.io/Hello-World-MLp>\
      <div class="comment-header">Commentshttp://hirohio.github.io/Hello-World-MLdiv>\
      <div class="comment-loading" id="cn<%id%>">\
        loading comments... <img src="<%loadingImage%>" alt=""http://hirohio.github.io/Hello-World-ML>http://hirohio.github.io/Hello-World-MLdiv>\
      <ul id="cl<%id%>" class="comment-ul">http://hirohio.github.io/Hello-World-MLul>\
      <div id="ca<%id%>">\
      <p class="add-a-comment">Add a comment\
        (<a href="#" class="comment-markup" id="ab<%id%>">markuphttp://hirohio.github.io/Hello-World-MLa>):http://hirohio.github.io/Hello-World-MLp>\
      <div class="comment-markup-box" id="mb<%id%>">\
        reStructured text markup: <i>*emph*http://hirohio.github.io/Hello-World-MLi>, <b>**strong**http://hirohio.github.io/Hello-World-MLb>, \
        <code>``code``http://hirohio.github.io/Hello-World-MLcode>, \
        code blocks: <code>::http://hirohio.github.io/Hello-World-MLcode> and an indented block after blank linehttp://hirohio.github.io/Hello-World-MLdiv>\
      <form method="post" id="cf<%id%>" class="comment-form" action="">\
        <textarea name="comment" cols="80">http://hirohio.github.io/Hello-World-MLtextarea>\
        <p class="propose-button">\
          <a href="#" id="pc<%id%>" class="show-propose-change">\
            Propose a change &#9657;\
          http://hirohio.github.io/Hello-World-MLa>\
          <a href="#" id="hc<%id%>" class="hide-propose-change">\
            Propose a change &#9663;\
          http://hirohio.github.io/Hello-World-MLa>\
        http://hirohio.github.io/Hello-World-MLp>\
        <textarea name="proposal" id="pt<%id%>" cols="80"\
                  spellcheck="false">http://hirohio.github.io/Hello-World-MLtextarea>\
        <input type="submit" value="Add comment"http://hirohio.github.io/Hello-World-ML>\
        <input type="hidden" name="node" value="<%id%>"http://hirohio.github.io/Hello-World-ML>\
        <input type="hidden" name="parent" value=""http://hirohio.github.io/Hello-World-ML>\
      http://hirohio.github.io/Hello-World-MLform>\
      http://hirohio.github.io/Hello-World-MLdiv>\
    http://hirohio.github.io/Hello-World-MLdiv>';

  var commentTemplate = '\
    <div id="cd<%id%>" class="sphinx-comment<%css_class%>">\
      <div class="vote">\
        <div class="arrow">\
          <a href="#" id="uv<%id%>" class="vote" title="vote up">\
            <img src="<%upArrow%>"http://hirohio.github.io/Hello-World-ML>\
          http://hirohio.github.io/Hello-World-MLa>\
          <a href="#" id="uu<%id%>" class="un vote" title="vote up">\
            <img src="<%upArrowPressed%>"http://hirohio.github.io/Hello-World-ML>\
          http://hirohio.github.io/Hello-World-MLa>\
        http://hirohio.github.io/Hello-World-MLdiv>\
        <div class="arrow">\
          <a href="#" id="dv<%id%>" class="vote" title="vote down">\
            <img src="<%downArrow%>" id="da<%id%>"http://hirohio.github.io/Hello-World-ML>\
          http://hirohio.github.io/Hello-World-MLa>\
          <a href="#" id="du<%id%>" class="un vote" title="vote down">\
            <img src="<%downArrowPressed%>"http://hirohio.github.io/Hello-World-ML>\
          http://hirohio.github.io/Hello-World-MLa>\
        http://hirohio.github.io/Hello-World-MLdiv>\
      http://hirohio.github.io/Hello-World-MLdiv>\
      <div class="comment-content">\
        <p class="tagline comment">\
          <span class="user-id"><%username%>http://hirohio.github.io/Hello-World-MLspan>\
          <span class="rating"><%pretty_rating%>http://hirohio.github.io/Hello-World-MLspan>\
          <span class="delta"><%time.delta%>http://hirohio.github.io/Hello-World-MLspan>\
        http://hirohio.github.io/Hello-World-MLp>\
        <div class="comment-text comment"><#text#>http://hirohio.github.io/Hello-World-MLdiv>\
        <p class="comment-opts comment">\
          <a href="#" class="reply hidden" id="rl<%id%>">reply &#9657;http://hirohio.github.io/Hello-World-MLa>\
          <a href="#" class="close-reply" id="cr<%id%>">reply &#9663;http://hirohio.github.io/Hello-World-MLa>\
          <a href="#" id="sp<%id%>" class="show-proposal">proposal &#9657;http://hirohio.github.io/Hello-World-MLa>\
          <a href="#" id="hp<%id%>" class="hide-proposal">proposal &#9663;http://hirohio.github.io/Hello-World-MLa>\
          <a href="#" id="dc<%id%>" class="delete-comment hidden">deletehttp://hirohio.github.io/Hello-World-MLa>\
          <span id="cm<%id%>" class="moderation hidden">\
            <a href="#" id="ac<%id%>" class="accept-comment">accepthttp://hirohio.github.io/Hello-World-MLa>\
          http://hirohio.github.io/Hello-World-MLspan>\
        http://hirohio.github.io/Hello-World-MLp>\
        <pre class="proposal" id="pr<%id%>">\
<#proposal_diff#>\
        http://hirohio.github.io/Hello-World-MLpre>\
          <ul class="comment-children" id="cl<%id%>">http://hirohio.github.io/Hello-World-MLul>\
        http://hirohio.github.io/Hello-World-MLdiv>\
        <div class="clearleft">http://hirohio.github.io/Hello-World-MLdiv>\
      http://hirohio.github.io/Hello-World-MLdiv>\
    http://hirohio.github.io/Hello-World-MLdiv>';

  var replyTemplate = '\
    <li>\
      <div class="reply-div" id="rd<%id%>">\
        <form id="rf<%id%>">\
          <textarea name="comment" cols="80">http://hirohio.github.io/Hello-World-MLtextarea>\
          <input type="submit" value="Add reply"http://hirohio.github.io/Hello-World-ML>\
          <input type="button" value="Cancel"http://hirohio.github.io/Hello-World-ML>\
          <input type="hidden" name="parent" value="<%id%>"http://hirohio.github.io/Hello-World-ML>\
          <input type="hidden" name="node" value=""http://hirohio.github.io/Hello-World-ML>\
        http://hirohio.github.io/Hello-World-MLform>\
      http://hirohio.github.io/Hello-World-MLdiv>\
    http://hirohio.github.io/Hello-World-MLli>';

  $(document).ready(function() {
    init();
  });
})(jQuery);

$(document).ready(function() {
 http://hirohio.github.io/Hello-World-ML/ add comment anchors for all paragraphs that are commentable
  $('.sphinx-has-comment').comment();

 http://hirohio.github.io/Hello-World-ML/ highlight search words in search results
  $("div.context").each(function() {
    var params = $.getQueryParameters();
    var terms = (params.q) ? params.q[0].splithttp://hirohio.github.io/Hello-World-ML\shttp://hirohio.github.io/Hello-World-ML) : [];
    var result = $(this);
    $.each(terms, function() {
      result.highlightText(this.toLowerCase(), 'highlighted');
    });
  });

 http://hirohio.github.io/Hello-World-ML/ directly open comment window if requested
  var anchor = document.location.hash;
  if (anchor.substring(0, 9) == '#comment-') {
    $('#ao' + anchor.substring(9)).click();
    document.location.hash = '#s' + anchor.substring(9);
  }
});
