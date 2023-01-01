clean:
	@rm -fr */.ipynb_checkpoints
	@rm -fr */*/.ipynb_checkpoints
	@rm -fr */*/*/.ipynb_checkpoints
	@rm -fr *.egg-info


run_api:
	uvicorn api.fast:app --reload


