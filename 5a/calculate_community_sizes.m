function [community_sizes, community_size_counts] = calculate_community_sizes(communities)
community_labels = unique(communities);
community_sizes = hist(communities, community_labels);
[community_size_counts, community_sizes] = hist(community_sizes, unique(community_sizes));
end

