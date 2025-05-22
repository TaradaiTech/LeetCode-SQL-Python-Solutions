import heapq

class Solution:
    def maxRemoval(self, nums, queries):
        # Sort queries by their start time
        queries.sort(key=lambda x: x[0])

        # Max-heap for available queries (store end times as negative values)
        available_queries = []
        # Min-heap for queries already assigned (store end times)
        assigned_queries = []

        total_used = 0
        query_index = 0

        for position in range(len(nums)):
            # Remove expired assigned queries (those ending before current position)
            while assigned_queries and assigned_queries[0] < position:
                heapq.heappop(assigned_queries)

            # Add queries that start on or before current position to available heap
            while query_index < len(queries) and queries[query_index][0] <= position:
                heapq.heappush(available_queries, -queries[query_index][1])  # max-heap
                query_index += 1

            # Assign enough queries to satisfy nums[position]
            while len(assigned_queries) < nums[position]:
                # No available queries that cover current position
                if not available_queries or -available_queries[0] < position:
                    return -1

                # Use the best available query (ends furthest in future)
                end = -heapq.heappop(available_queries)
                heapq.heappush(assigned_queries, end)
                total_used += 1

        # Return how many queries are unused
        return len(queries) - total_used