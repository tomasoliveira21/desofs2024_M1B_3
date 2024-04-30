TAG = latest
DOCKER_LOCAL = socialnet-backend:$(TAG)
DOCKER_REPO = something.dkr.ecr.us-west-2.amazonaws.com/socialnet-backend
DOCKER_REMOTE = $(DOCKER_REPO):$(TAG)

.PHONY: build
build:
	docker build -t $(DOCKER_LOCAL) --build-arg FURY_AUTH .

push:
	docker tag $(DOCKER_LOCAL) $(DOCKER_REMOTE)
	docker push $(DOCKER_REMOTE)

buildpush: build push

buildproto:
	socialNet_backend/api/grpc/makeprotobufs

proto: buildproto
	mkdir -p dist && \
	cp -r socialNet_backend/api/grpc/dist/*.tar.gz dist

taskdefs:
	cd deployment && ./compile.py taskdefs

buildspecs:
	cd deployment && ./compile.py buildspecs
