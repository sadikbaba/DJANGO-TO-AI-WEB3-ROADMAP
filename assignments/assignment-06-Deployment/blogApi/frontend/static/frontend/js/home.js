async function loadCategories() {
    const select = document.getElementById("category");

    try {
        const response = await apiFetch("/categories/");
        const data = await response.json();

        select.innerHTML = "";

        if (data.results.length === 0) {
            select.innerHTML = '<option value="">No categories yet</option>';
            return;
        }

        data.results.forEach(function (category) {
            const option = document.createElement("option");
            option.value = category.id;
            option.textContent = category.name;
            select.appendChild(option);
        });

    } catch (error) {
        select.innerHTML = '<option value="">Could not load categories</option>';
        console.error(error);
    }
}

function setupAutoResizeTextarea() {
    const textarea = document.getElementById("content");

    if (!textarea) {
        return;
    }

    textarea.addEventListener("input", function () {
        this.style.height = "auto";
        this.style.height = Math.min(this.scrollHeight, 300) + "px";
    });
}

function setupCreatePostForm() {
    const section = document.getElementById("create-post-section");
    const form = document.getElementById("create-post-form");
    const message = document.getElementById("create-post-message");

    if (!isLoggedIn()) {
        return;
    }

    section.style.display = "block";
    loadCategories();

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const title = document.getElementById("title").value;
        const content = document.getElementById("content").value;
        const category = document.getElementById("category").value;

        try {
            const response = await apiFetch("/posts/", {
                method: "POST",
                body: JSON.stringify({ title, content, category }),
            });

            const data = await response.json();

            if (response.ok) {
                message.textContent = "Post created!";
                form.reset();
                loadPosts();
            } else {
                message.textContent = "Failed: " + JSON.stringify(data);
            }
        } catch (error) {
            message.textContent = "Something went wrong.";
            console.error(error);
        }
    });
}



setupCreatePostForm();
setupAutoResizeTextarea();


function enterEditMode(postElement, post) {
    const body = postElement.querySelector(".post-body");
    const footer = postElement.querySelector(".post-footer");

    body.innerHTML = `
    <input type="text" class="edit-title-input" value="${post.title}">
    <textarea class="edit-content-input">${post.content}</textarea>
`;

    footer.innerHTML = "";

    const saveButton = document.createElement("button");
    saveButton.textContent = "Save";
    saveButton.classList.add("save-btn");

    const cancelButton = document.createElement("button");
    cancelButton.textContent = "Cancel";
    cancelButton.classList.add("cancel-btn");

    saveButton.addEventListener("click", async function () {
        const newTitle = postElement.querySelector(".edit-title-input").value;
        const newContent = postElement.querySelector(".edit-content-input").value;

        const response = await apiFetch(`/posts/${post.id}/`, {
            method: "PATCH",
            body: JSON.stringify({ title: newTitle, content: newContent }),
        });

        if (response.ok) {
            loadPosts();
        } else {
            alert("Could not update post.");
        }
    });

    cancelButton.addEventListener("click", function () {
        loadPosts();
    });

    footer.appendChild(saveButton);
    footer.appendChild(cancelButton);
}

async function loadPosts() {
    const container = document.getElementById("posts-container");
    container.innerHTML = "<p>Loading posts...</p>";

    try {
        const response = await apiFetch("/posts/");
        const data = await response.json();
        const posts = data.results || [];

        container.innerHTML = "";

        if (posts.length === 0) {
            container.innerHTML = "<p>No posts yet.</p>";
            return;
        }

        posts.forEach(post => {
            const postElement = document.createElement("div");
            postElement.classList.add("post-card");

            const CHAR_LIMIT = 200;
            const isLong = post.content.length > CHAR_LIMIT;
            const preview = isLong ? post.content.slice(0, CHAR_LIMIT) + "..." : post.content;

            const isAuthor = isLoggedIn() && String(post.author_id) === String(getCurrentUserId());

            postElement.innerHTML = `
                <div class="post-header">
                    <h3>${post.title}</h3>
                    <p class="post-meta">
                        By ${post.author} in ${post.category_name || 'Uncategorized'} • ${post.views || 0} views
                    </p>
                </div>

                <div class="post-body">
                    <p class="post-content">${isLong ? preview : post.content}</p>
                    ${isLong ? '<a href="#" class="read-more-link">Read More</a>' : ""}
                </div>

                <div class="post-footer">
                    <button class="like-btn" data-post-id="${post.id}">❤️ ${post.likes_count || 0}</button>
                    <button class="bookmark-btn" data-post-id="${post.id}">🔖 ${post.bookmarks_count || 0}</button>
                    <button class="comment-toggle" data-post-id="${post.id}">💬 ${post.comments_count || 0}</button>
                    ${isAuthor ? `
                        <button class="edit-btn">Edit</button>
                        <button class="delete-btn">Delete</button>
                    ` : ''}
                </div>

                <div class="comments-section" id="comments-${post.id}" style="display:none; margin-top:15px;">
                    <div class="comment-list"></div>
                    ${isLoggedIn() ? `
                        <textarea class="new-comment" placeholder="Write a comment..." style="width:100%;"></textarea>
                        <button class="post-comment-btn" data-post-id="${post.id}">Post Comment</button>
                    ` : '<p style="color:#666; margin-top:10px;">Login to comment</p>'}
                </div>
            `;

            container.appendChild(postElement);

            // Restore Read More functionality
            if (isLong) {
                const contentEl = postElement.querySelector(".post-content");
                const toggleLink = postElement.querySelector(".read-more-link");
                let expanded = false;

                toggleLink.addEventListener("click", function (e) {
                    e.preventDefault();
                    expanded = !expanded;
                    contentEl.textContent = expanded ? post.content : preview;
                    toggleLink.textContent = expanded ? "Read Less" : "Read More";
                });
            }

            // New buttons
            postElement.querySelector('.like-btn').addEventListener('click', () => toggleLike(post.id));
            postElement.querySelector('.bookmark-btn').addEventListener('click', () => toggleBookmark(post.id));
            postElement.querySelector('.comment-toggle').addEventListener('click', () => toggleComments(post.id, postElement));
        });

    } catch (e) {
        console.error(e);
        container.innerHTML = "<p>Error loading posts.</p>";
    }
}

loadPosts();


async function toggleLike(postId, postElement) {
    await apiFetch(`/api/likes/`, { method: "POST", body: JSON.stringify({post: postId}) });
    loadPosts(); // refresh
}

async function toggleBookmark(postId, postElement) {
    await apiFetch(`/api/bookmarks/`, { method: "POST", body: JSON.stringify({post: postId}) });
    loadPosts();
}

async function toggleComments(postId, postElement) {
    const section = document.getElementById(`comments-${postId}`);
    section.style.display = section.style.display === 'none' ? 'block' : 'none';
    // load comments logic can be added later
}


// Load comments for a post
async function loadComments(postId, postElement) {
    const commentList = postElement.querySelector('.comment-list');
    commentList.innerHTML = "Loading comments...";

    try {
        const response = await apiFetch(`/api/comments/?post=${postId}`);
        const comments = await response.json();

        commentList.innerHTML = "";

        // Simple flat list for now (we can make nested later)
        comments.results.forEach(comment => {
            const div = document.createElement("div");
            div.style.margin = "10px 0";
            div.style.padding = "10px";
            div.style.borderLeft = "3px solid #2563eb";
            div.innerHTML = `
                <strong>${comment.author}</strong> 
                <small>${new Date(comment.created_at).toLocaleString()}</small>
                <p>${comment.content}</p>
            `;
            commentList.appendChild(div);
        });

        if (comments.results.length === 0) {
            commentList.innerHTML = "<p>No comments yet.</p>";
        }
    } catch (e) {
        commentList.innerHTML = "<p>Could not load comments.</p>";
    }
}

// Toggle comments + load them
async function toggleComments(postId, postElement) {
    const section = document.getElementById(`comments-${postId}`);
    const isHidden = section.style.display === 'none';

    section.style.display = isHidden ? 'block' : 'none';

    if (isHidden) {
        await loadComments(postId, postElement);
    }
}

// Post a new comment
document.addEventListener('click', async function(e) {
    if (e.target.classList.contains('post-comment-btn')) {
        const postId = e.target.dataset.postId;
        const textarea = e.target.parentElement.querySelector('.new-comment');
        const content = textarea.value.trim();

        if (!content) return;

        try {
            await apiFetch('/comments/', {
                method: 'POST',
                body: JSON.stringify({ post: postId, content: content, parent: null })
            });
            textarea.value = '';
            loadComments(postId, e.target.closest('.post-card')); // refresh comments
        } catch (err) {
            alert("Failed to post comment");
        }
    }
});