const Router = ReactRouter.Router;
const Route = ReactRouter.Route;
const browserHistory = ReactRouter.browserHistory;

//global variable to store origin url (e.g http://localhost:5000)
const latest_api =  window.location.origin + '/api/v1.0/latest';

const LatestEntries = React.createClass({
    getInitialState: function(){
        return {
            photos: [],
            favorite_photo: ''
        };
    },

    handleFavoriteClick: function(e) {
        e.preventDefault();
        var title = this.state.title;
        var options = this.state.options;

        var data = {'title': title, options: options.map(function(x){return x.name})};
        var url =  origin + '/api/polls'

        // make post request
        $.ajax({
          url: url,
          dataType: 'json',
          type: 'POST',
          data: JSON.stringify(data),
          contentType: 'application/json; charset=utf-8',
          success: function(data){
            alert(data.message);
          }.bind(this),
          error: function(xhr, status, err){
            alert('Poll creation failed: ' + err.toString());
          }.bind(this)
        });
      },

    render: function(){
        const photos = this.props.photos.map((photo, index) =>
            <div key={photo.id}>
                <div className="row">
                    <div className="col-md-8">
                        <h4>{photo.title}</h4>
                        <a href={photo.link}><img src={photo.media} alt={photo.title} /></a>

                    </div>
                    <div className="col-md-4">
                        <button className="btn btn-success" id={photo} onClick={this.handleFavoriteClick}>
                          <span className="glyphicon glyphicon-star"></span> Fave
                        </button>
                        <br />
                        <p><strong>Taken on</strong> {photo.date_taken} <strong>by</strong> <a href={photo.author_id || "Anonymous"} target="_blank">{photo.author}</a></p>
                        <br />
                        <p><strong>Tags: </strong>{photo.tags}</p>
                    </div>
                </div>
                <br /><br />
                <hr />
            </div>
        );

        return (
          <div>
              {photos}
          </div>
        );
  }
});

const Latest = React.createClass({
    getInitialState: function(){
        return {
            photos: []
        };
    },

    // Used to poll as soon as we hit the page, and then every 60 seconds later.
    startPolling: function() {
        var self = this;
        setTimeout(function() {
          self.getLatestPosts();
          self._timer = setInterval(self.getLatestPosts.bind(self), 60000);
        }, 1000);
    },

    // get the latest posts from our backend API.
    getLatestPosts: function(){
        $.ajax({
            url: latest_api,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({photos: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(latest_api, status, err.toString());
            }.bind(this)
        });
    },

    componentDidMount: function(){
        this.startPolling();
    },

    componentWillUnmount: function() {
        if (this._timer) {
          clearInterval(this._timer);
          this._timer = null;
        }
    },

    render: function(){
        return (<LatestEntries photos={this.state.photos} />);
    }
});

ReactDOM.render((
  <Router history={browserHistory}>
      <Route path="/" component={Latest} />
  </Router>
  ),
  document.getElementById('data-container')
);