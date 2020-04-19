clear
close all

%% Read data
T = readtable('communities.csv', 'ReadVariableNames', true);
kclique = table2array(T(:, 15));
demon =  table2array(T(:, 16));
louvain = table2array(T(:, 17));
infomap = table2array(T(:, 18));

% 0 means community with size 1, make these labels unique also
kclique(kclique==0) = 2000:2000+length(kclique(kclique==0))-1;
demon(demon==0) = 2000:2000+length(demon(demon==0))-1;

%% Number of communities
count_kclique = length(unique(kclique))
count_demon = length(unique(demon))
count_louvain = length(unique(louvain))
count_infomap = length(unique(infomap))

%% Community size distribution
[klique_sizes, klique_size_counts] = calculate_community_sizes(kclique);
[demon_sizes, demon_size_counts] = calculate_community_sizes(demon);
[louvain_sizes, louvain_size_counts] = calculate_community_sizes(louvain);
[infomap_sizes, infomap_size_counts] = calculate_community_sizes(infomap);

figure
loglog(klique_sizes, klique_size_counts, '.', 'MarkerSize', 15)
hold on;
loglog(demon_sizes, demon_size_counts, '.', 'MarkerSize', 15)
loglog(louvain_sizes, louvain_size_counts, '.', 'MarkerSize', 15)
loglog(infomap_sizes, infomap_size_counts, '.', 'MarkerSize', 15)

xlabel('Number of nodes in the community')
ylabel('Number of communities')
title('Community size distribution')
legend('K-clique', 'Demon', 'Louvain', 'Infomap')
ylim([0.5 1500])