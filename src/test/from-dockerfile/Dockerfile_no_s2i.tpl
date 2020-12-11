FROM #IMAGE_NAME# # Replaced by sed in tests, see test_from_dockerfile in test/run

# Add application sources
USER 0
ADD app-src .

# Install the dependencies
RUN pip install -U "pip>=19.3.1" && \
    pip install -r requirements.txt && \
    python manage.py collectstatic --noinput && \
    python manage.py migrate

# Run the application
CMD python manage.py runserver 0.0.0.0:8080
