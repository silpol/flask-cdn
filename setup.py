import setuptools


setuptools.setup(
    name='Flask-CDN',
    version='1.5.1',
    url='https://libwilliam.github.io/flask-compress/',
    license='MIT',
    author='William Fagan',
    author_email='libwilliam@gmail.com',
    description='Serve the static files in your Flask app from a CDN.',
    long_description='Full documentation can be found on the Flask-CDN "Home Page".',
    py_modules=['flask_cdn'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
