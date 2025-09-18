use std::collections::{HashMap, BTreeSet};
use std::cmp::Ordering;

#[derive(Debug, PartialEq, Eq)]
struct Task {
    user_id: i32,
    task_id: i32,
    priority: i32,
}

impl PartialOrd for Task {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Task {
    fn cmp(&self, other: &Self) -> Ordering {
        match other.priority.cmp(&self.priority) {
            Ordering::Equal => other.task_id.cmp(&self.task_id),
            other_ord => other_ord,
        }
    }
}

struct TaskManager {
    queue: BTreeSet<Task>,
    task_to_details: HashMap<i32, (i32, i32)>,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TaskManager {

    fn new(tasks: Vec<Vec<i32>>) -> Self {
        let mut queue = BTreeSet::new();
        let mut task_to_details = HashMap::new();
        for task in tasks {
            queue.insert(Task {
                user_id: task[0],
                task_id: task[1],
                priority: task[2],
            });
            task_to_details.insert(task[1], (task[0], task[2]));
        }
        Self {
            queue,
            task_to_details
        }
    }

    fn add(&mut self, user_id: i32, task_id: i32, priority: i32) {
        self.queue.insert(Task {
            user_id,
            task_id,
            priority,
        });
        self.task_to_details.insert(task_id, (user_id, priority));
    }

    fn edit(&mut self, task_id: i32, new_priority: i32) {
        self.rmv(task_id);
        if let Some((user_id, priority)) = self.task_to_details.get(&task_id) {
            self.queue.insert(Task {
                user_id: *user_id,
                task_id,
                priority: new_priority,
            });
            self.task_to_details.insert(task_id, (*user_id, new_priority));
        }
    }

    fn rmv(&mut self, task_id: i32) {
        if let Some((user_id, priority)) = self.task_to_details.get(&task_id) {
            self.queue.remove(&Task {
                user_id: *user_id,
                task_id,
                priority: *priority,
            });
        }
    }

    fn exec_top(&mut self) -> i32 {
        self.queue
            .pop_first()
            .unwrap_or(Task {
                user_id: -1,
                task_id: -1,
                priority: -1,
            }).user_id
    }
}

/**
 * Your TaskManager object will be instantiated and called as such:
 * let obj = TaskManager::new(tasks);
 * obj.add(userId, taskId, priority);
 * obj.edit(taskId, newPriority);
 * obj.rmv(taskId);
 * let ret_4: i32 = obj.exec_top();
 */
