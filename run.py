from myapp import create_app, db


if __name__ == '__main__':
    app = create_app()
    '''with app.app_context():
        db.drop_all()
        db.create_all()'''
    app.run()
    # host='0.0.0.0'
