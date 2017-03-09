const Router = ReactRouter.Router;
const Route = ReactRouter.Route;
const browserHistory = ReactRouter.browserHistory;

//global variable to store origin url (e.g http://localhost:5000)
const origin = window.location.origin;
const favorites_api =  origin + '/api/v1.0/favorites';

const FavoriteEntry = React.createClass({
    getInitialState: function(){
        return {
            photos: []
        };
    },

    unFave: function(){

        //make get request
        $.ajax({
            url: api,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({photos: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(api, status, err.toString());
            }.bind(this)
        });
    },

    render: function(){
        const photos = this.props.photos.map((photo, index) =>
            <div>
                <div className="row" key={photo.id}>
                    <div className="col-md-8">
                        <h4>{photo.title}</h4>
                        <a href={photo.link}><img src={photo.media} alt={photo.title} /></a>

                    </div>
                    <div className="col-md-4">
                        <form onSubmit={this.unstar}>
                            <a href="#" className="btn btn-danger"><span className="glyphicon glyphicon-star-empty"></span> unFave</a>
                        </form>
                        <br />
                        <p><strong>Taken on</strong> {photo.date_taken} <strong>by</strong> <a href={photo.author_id} target="_blank">{photo.author}</a></p>
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

const Favorites = React.createClass({
    getInitialState: function(){
        return {
            photos: []
        };
    },

    getFavorites: function(){
        $.ajax({
            url: favorites_api,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({photos: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(favorites_api, status, err.toString());
            }.bind(this)
        });
    },

    componentDidMount: function(){
        this.getFavorites();
    },

    render: function(){
        return (<FavoriteEntry photos={this.state.photos} />);
    }
});

ReactDOM.render((
  <Router history={browserHistory}>
      <Route path="/favorites" component={Favorites} />
  </Router>
  ),
  document.getElementById('data-container')
);