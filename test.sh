#!/bin/sh
echo "total"
ls -l exp_results | wc -l

echo "my"
python run_experiment.py --taurus --workload my --n_array_jobs 1 --array_job_id 0 --dry_run  | wc -l
echo "baselines"
python run_experiment.py --taurus --workload baselines --n_array_jobs 1 --array_job_id 0 --dry_run  | wc -l
echo "passive"
python run_experiment.py --taurus --workload passive --n_array_jobs 1 --array_job_id 0 --dry_run  | wc -l
echo "trustscore"
python run_experiment.py --taurus --workload trustscore --n_array_jobs 1 --array_job_id 0 --dry_run  | wc -l
