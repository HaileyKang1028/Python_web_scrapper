from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file


print("============================================")
so_jobs = get_so_jobs()
print("============================================")
indeed_jobs = get_indeed_jobs()
print("============================================")
jobs = indeed_jobs + so_jobs
print("============================================")
save_to_file(jobs)
